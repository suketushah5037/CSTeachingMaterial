<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: text/json;");

//function set_value($isbn)
//{	
	#the "isbn" value
	#handler.response.headers['Content-Type'] = 'application/jsonrequest';
	//echo "inside set_value";
	#make a json and set the value of isbn
	//json.dump(["VALUE", "isbn", $isbn], handler.response.out);
	
    #Commented lines of code - might be useful later
    //$key =  "D6ONXMNB";
    //$url = "isbndb.com/api/v2/json/".$key."/book/".$isbn;
    // echo $url;
    
    
    //$curl = curl_init();  
    //curl_setopt($curl,CURLOPT_URL,$url);
    //curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
    //curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
    //$curlData = curl_exec($curl);
    //curl_close($curl);
    
    // echo $curlData;
    //dont use true - need an object not an array
    //$json = json_decode($curlData,true);
    
    //var_dump($json->{'data'});
    //var_dump($json['data']['0']['author_data']);
    
    //echo $json['data']['0']['author_data']->{'notes'};
    
    //$author_name = "";
    //foreach($json['data']['0']['author_data'] as $data)
    //{
      //  $author_name = $data['name'];
        //echo $data['name'];
        //echo $data['id'];
    //}
    // return $author_name;

    
   // $content =file_get_contents ('isbndb.com/api/v2/json/D6ONXMNB/book/9781593277499');
   // $data =JSON.parse($content) ;
   // echo $data;
   #Commented lines of code - might be useful later
    
//}

#Commented lines of code - might be useful later
//isbndb.com/api/v2/json/D6ONXMNB/book/9780131988132
//http://isbndb.com/api/books.xml?//access_key=D6ONXMNB&index1=isbn&value1=9781593277499
//making page to behave like xml document to show xml
//header('Content-Type:text/xml; charset=UTF-8');
//calling function
//$isbn_number = "9780131988132";
//$xml = store_isbn($isbn_number);
//$resultData = array("VALUE","author",array($xml));
//$resultDataJSON = json_encode($resultData);
//echo $resultDataJSON;
//echo $xml;
#Commented lines of code - might be useful later

#. for concatenation

#print_var for not an object $_GET for the url parameters sent in post req
#http://192.168.1.16/setvalue?tag=isbn&value=9780131988132
#var_dump($_GET);
#$tag = $_POST['tag'];
#echo $tag;
#$value = $_POST['value'];
#echo $value;

#$tag = $_POST['tag'];
#echo $tag;
#$value = $_POST['value'];
#echo $value;
#$value=$_POST['value'];

#echo $value;".$key."
#$retval = array("VALUE", $tag, "\"".$value."\"");
#echo json_encode($retval);
#["VALUE","isbn","9780131988132"]
#file_put_contents('isbnval.txt', json_encode($retval));
#["VALUE","isbn","9780131988132"]
#session_start();
#$_SESSION['isbndata'] = $retval;
#echo json_encode($_SESSION);
#{"isbndata":["VALUE","isbn","9780131988132"]}


# ["STORED", "firstName", "\"Lewis\""]
$tag = $_POST['tag'];
$value = $_POST['value'];

#Create an array
#Needs a "VALUE" ["VALUE", "contacts", ["Lewis Moten", "John Smith", "Jane Doe"]]
#or directly store the isbn number
#$retval = array("VALUE", $tag, "\"".$value."\"");
#echo json_encode($retval);

#store in a file
#file_put_contents('isbnval.txt', json_encode($retval));

#store only the isbn in the file
#store a value without quotes
$value = trim($value,'"');
file_put_contents('isbnval.txt', $value);

#Store in session
#session_start();
#$_SESSION['isbndata'] = $retval;
?>

