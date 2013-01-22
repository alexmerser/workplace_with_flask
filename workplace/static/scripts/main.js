function daysInMonth(month,year) {
   return new Date(year, month, 0).getDate();
}


jQuery(document).ready(function ($) {
	

	// Birthday Logic
 	var $birthday_month = $('#birthday_month');  
 	var $birthday_day = $('#birthday_day');
 	var $birthday_year = $('#birthday_year');

 	// Fill birth years from js to have a dynamic list
	var bday_years = ['<option value="-1">Year: </option>'];
	var current_year = new Date().getFullYear();
	for(var i = current_year; i >= 1905; i--) {
		bday_years.push('<option value="' + i + '">' + i + '</option>');
	}  
 	$birthday_year.html(bday_years.join(''));

 	// Do not allow to add something like 30th of feb, thus update no of days accordingly.
 	$birthday_year.add($birthday_month).change(function () {
 		var selected_year = $birthday_year.val();
 		var selected_month = $birthday_month.val()
 		if( selected_year != -1 && selected_month != -1 ) {
 			var bday_days = ['<option value="-1">Day:</option>'];
 			var days_in_month = daysInMonth(selected_month,selected_year);
 			for(var i = 1; i <= days_in_month; i++ ) {
 				bday_days.push('<option value="' + i + '">' + i + '</option>');
 			} 
 			var selected_day = $birthday_day.val(); 
 			$birthday_day.html(bday_days.join('')).val(selected_day);
 		}
 	}); 



	//$('select').dropkick(); 

	$('#add_news').focus(function () {
		var $this = $(this);
		$this.attr('rows',5); 
		$('#privacy_buttons').show();
	})	

	var archives = $('#archives');

	$('#archive_action_list').find('a').click(function () {
		archives.find('.noticebar').html('');
		var target = $(this).attr('href')
		archives.find('form').hide();
		$(target).fadeIn('fast');
		return false;
	});

	var action_buttons = archives.find('.action_buttons');
	action_buttons.find('[data-type="add"]').click(function () {
		var $this = $(this);
		var parent = $this.closest('form'); 
		var params = { 
			'type' 		  : $this.data('type'),
			'action'  	  : $this.data('action'),
			'content' 	  : parent.find('textarea[name="content"]').val(),
			'description' : parent.find('input[name="description"]').prop('value'),
			'tags'		  : parent.find('input[name="tags"]').prop('value')
		}
		console.log(params);
		$.post('', params, function (response) {
			var response = "The response sent from server";
			archives.find('.noticebar').html(response);
			archives.find('form').hide()
		})
	});

	

	$('#sort_news').change(function () {
		var params = {
			'action' 	: 'sort_news',
			'orderby'	: $(this).val()
		}
		$.post('', params, function (response) {
			
		});
	});

	var news_articles_wrapper = $('#news_articles_wrapper');

	 

	news_articles_wrapper.find('.news_wrapper').hover(function () {
		var $this = $(this);
		$this.find('.action_wrapper').show();
	}, function () {
		var $this = $(this); 
		var action_wrapper = $this.find('.action_wrapper');
		if(!action_wrapper.find('ul').is(':visible')){
			action_wrapper.hide();
		}
	});

	$('#todos').find('input[type="checkbox"]').change(function () {
		$(this).parent().toggleClass('striked');
	});

	$('[data-toggler]').each(function () {
		var $this = $(this);
		$this.on($this.data('toggler'),function () { 
			$this.next().toggle();
		});
	})

	var select = $('.select')
	select.on('click','li > a', function () {
		var $this = $(this); 
		$this.closest('.select').find('.active').removeClass('active');
		$this.addClass('active');
		var clicker = $this.closest('.select').find('a').eq(0);
		if(!clicker.hasClass('action_button')) {
			var html = $(this).html(); 
			clicker.html(html);
		} 
		$this.closest('ul').hide();
		return false;
	})

	$('.comment_link').click(function () {
		var $this = $(this);
		$this.closest('.news_wrapper').find('.news_reply').find('input:last').focus();
		return false;
	});


	
	var tags = $('#tags');
	tags.on('click', '.clear_btn', function () {
		$(this).parent().remove();
		return false;
	});

	var tags_source = [];
	$('#tags_input')
		.typeahead({
			source: function (query, process) {   
				if(tags_source.length !==0) {
					return tags_source;
				}
				$.get('server.php', { action: 'tags', query: query }, function (data) {
		        	tags_source = $.map(data,function (obj) {
		         		return obj.title;
		         	}); 
		         	return process(tags_source);
		        });
		    },
		    updater:function (item) { 
		       	tags.append('<div class="tag clearfix"><span class="title">' + item + '</span><a href="#" class="clear_btn fr">clear</a></div>');
				return '';
		    }
		});
 
	$.get('server.php',{ action: 'get_network'}, function (list) {
		var privacy_list = '<li><a href="#" data-action="me">Only Me</a></li>';
		for(var i = 0,len = list.length; i < len ; i++) {
			privacy_list += '<li><a href="#" data-action="' + list[i] + '">' + list[i] + '</li>';
		}
		privacy_list += '<li><a href="#" data-action="public">Public</a></li>';
		$('[data-bind="privacy_list"]').html(privacy_list);
	});
	

	// a/list page

	var lists = $('#lists').on('click', 'li',function () {
		$('#list_members_wrapper').fadeIn('slow');
	});

	$('#create_list').click(function () {
		var list = $('#list_name') 
		lists.append('<li><a href="#">' + list.prop('value') + ' (0)</a></li>');
		list.prop('value','');
		// Request to server
		// var params = {};
		// $.post('', params, function () {
		// 	// If response is not okay, give 'try again' or disable like facebook
		// 	lists.find('li:last').addClass('disable');
		// });

		return false;
	});

	$('#add_friend_to_list').click(function () {
		var friend = $('#friend_to_add_to_list');
		$('#list_members').append('<li><a href="#">' + friend.prop('value')  + '</a></li>');
		friend.prop('value','');
		return false;
	});
});