<?php
	if(isset($_GET['action'])) {
		$action = $_GET['action']; 
		switch ($action) {
			case "tags": 
			
			$response = array( 
				array(
					"id"		=> "tag1",
					"title"		=> "success",
					"last_used" => "2023333"
				),
				array( 
					"id"		=> "tag2",
					"title"		=> "young",
					"last_used"	=> "2299222"
				),
				array( 
					"id"		=> "tag3",
					"title"		=> "people",
					"last_used"	=> "49883838"
				),
				array(
					"id"		=> "tag4",
					"title"		=> "puppies",
					"last_used"	=> "4994944"
				),
				array(
					"id"		=> "tag5",
					"title"		=> "abra ka dabra",
					"last_used" => "2023333"
				),
				array(
					"id"		=> "tag6",
					"title"		=> "docu",
					"last_used" => "2023333"
				)
			);

			break; 

			default:
			$response = "error";
		}

		header('Content-type: application/json;charset=utf-8');
		echo json_encode($response);
	}	
?>