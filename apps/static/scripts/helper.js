// placeholder for IE
    $(document).ready(function() {
        function add() {
            if($(this).val() === ''){
                $(this).val($(this).attr('placeholder')).addClass('placeholder');
            }
        }

        function remove() {
            if($(this).val() === $(this).attr('placeholder')){
                $(this).val('').removeClass('placeholder');
            }
        }

        // Create a dummy element for feature detection
        if (!('placeholder' in $('<input>')[0])) {

            // Select the elements that have a placeholder attribute
            $('input[placeholder], textarea[placeholder]').blur(add).focus(remove).each(add);

            // Remove the placeholder text before the form is submitted
            $('form').submit(function(){
                $(this).find('input[placeholder], textarea[placeholder]').each(remove);
            });
        }
    });
// -----------------------------------------------------------------------------------

// -----------------------------------------------------------------------------------
$("#btn_signup").live("click", function (e) { 
	if ($("#txt_firstname").val().length <= 0) {		
		showerror("Please enter first name !");
		return false;
	}	
	if ($("#txt_lastname").val().length <= 0) {		
		showerror("Please enter last name !");
		return false;
	}
	if ($("#txt_email").val().length <= 0) {		
		showerror("Please enter email !");
		return false;
	}
	if ($("#txt_email2").val().length <= 0) {		
		showerror("Please re-enter email !");
		return false;
	}
	if ($("#txt_password").val().length <= 0) {		
		showerror("Please enter password !");
		return false;
	}
	if ($("#txt_password2").val().length <= 0) {		
		showerror("Please re-enter password !");
		return false;
	}
	$(".error_block").fadeOut(500);
	return true;
	   
});

function showerror(txt) { 
	$(".error_block").text(txt).fadeIn(500); 
}

