

<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: text/json;");


#Scraper to get the author's name
function check_isbn($isbn)
{
    /*Key received by logging in into the isbn website for API
    #Visit this link for creating a key to use the API
    #http://isbndb.com/account/logincreate
    #URL format:  http://isbndb.com/api/v2/json/D6ONXMNB/book/9780131988132*/

    #Hardcoded
    #$url =  "isbndb.com/api/v2/json/D6ONXMNB/book/9780131988132";
    
    #My key
    $key =  "D6ONXMNB";
    
    #concatenate the URL
    $url = "isbndb.com/api/v2/json/".$key."/book/".$isbn;
    #echo $url;
     /*curl is a multi-protocol tool for viewing and downloading remote files.
 	Let's you make HTTP requests in PHP. 

	Need to install libcURL package for it
	In C:\wamp64\bin\php\php7.0.10\php.ini: 	
	
	Uncomment extension=php_curl.dll (Remove the ';')
	allow_url_fopen = On for HTTP requests without curl*/
    
    #Initialize cURL
    $curl = curl_init();  
    #Pass the URL
    curl_setopt($curl,CURLOPT_URL,$url);
    #other options
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);

    #Execute to get the data from the URL
    $curlData = curl_exec($curl);

    #Close it
    curl_close($curl);
    
    #The JSON data
    #echo $curlData;
    $json = json_decode($curlData,true);
    
    #cant echo a json directly
    #echo $json;
    
    #Scrape the author's name
    $author_name = "";
    foreach($json['data']['0']['author_data'] as $data)
    {
        $author_name = $data['name'];
        //echo $data['name'];
        //echo $data['id'];
    }
    return $author_name;

   
}


#Converts json data to a php string
#http://192.168.1.16/getvalue?tag=isbn

#Passed via HTTP Post from App Inventor
#when it comes from the URL use $_GET
#This is used for testing purposes to test the URL on the browser using http://192.168.1.7/getvalue?tag=isbn
$tag = $_POST['tag'];

$value = '';
#tag = author - sent from AppInventor
if($tag)
{
    #get key and value from a file stored on the web server
    #The file has just the isbn number stored without quottes using setvalue
    
    $value = file_get_contents('isbnval.txt');
    
}

#Pass the isbn number to parse the json data and just get the author's name
$xml = check_isbn($value);
#echo $xml;

#make it an array with tag "VALUE" as required by APPInventor, key "author" and value as the author's name received from check_isbn function
#app inventor code does not loop for array items, hence use the format for a single item - ok on the browser since it is an echo
#Required format
#["VALUE", "firstName", "\"Lewis\""]
#["VALUE", "contacts", ["Lewis Moten", "John Smith", "Jane Doe"]]

#add single quotes to the author's name and send as is - without this the json format is not acheived 
$valuetext = "'".$xml."'";
#echo $valuetext;

#Send it as an array
$resultData = array("VALUE","author", $valuetext);
#echo $resultData;

#encode it in JSON
$resultDataJSON = json_encode($resultData);

#HARDCODED for testing bugs
#echo it, to retreive the contents - hardcoded
#$resultData = array("VALUE","author",array('peter'));
#$resultDataJSON = json_encode($resultData);

#THE RESULT
echo $resultDataJSON;

?>

