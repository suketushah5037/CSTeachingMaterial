

<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: text/json;");


#Scraper to get the author's name
function check_isbn($isbn)
{
    /*Key received by logging in into the isbn website for API
    #Visit this link for creatig a key to use the API
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
    #echo $curlData;
    $json = json_decode($curlData,true);
    #cant echo a json directly
    #echo $json;
  
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
#$tag = "["VALUE", "isbn", "9780131988132"]";
#http://192.168.1.16/getvalue?tag=isbn

#Passed via HTTP Post from App Inventor
#$tag = $_POST['tag'];
#echo $tag;


#when it comes from the URL
$tag = $_POST['tag'];

$value = '';
#tag = author
if($tag)
{
    #get key and value from a file stored on the web server
    $value = file_get_contents('isbnval.txt');
    #$arr = array("VALUE",$tag, $value );
    #echo $_SESSION;
    #echo $value;
}
#["VALUE","tag","\"\"9780131988132\"\""] - contents of the file
#$messageType = json_decode($value);
#pick up the isbn number from the array
#pick the isbn number
#$isbn_number =  $messageType[2];
#echo $isbn_number;
#visit the webpage and scrape the content

#$xml = check_isbn($isbn_number);
$xml = check_isbn($value);
#echo $xml;
#make it an array with tag "VALUE" as required by APPInventor, key "author" and value as the author's name received from check_isbn function
#$resultData = array("VALUE","author",array($xml));
#app inventor is not able to parse an array for a single item returned - ok on the broswer since it is an echo

#["VALUE", "firstName", "\"Lewis\""]

#escape slash
#$addslash = "\\";
#echo $addslash;
#$addquoteswithslash = $addslash."\"";
$addquotes = "\"";
#echo $addquoteswithslash;
#$valuetext = $addquotes.$xml.$addquotes;
$valuetext = "'".$xml."'";
#echo $valuetext;

$resultData = array("VALUE","author", $valuetext);
#echo $resultData;
#encode it in JSON
$resultDataJSON = json_encode($resultData);

#echo it, to retreive the contents - hardcoded
#$resultData = array("VALUE","author",array('peter'));
#$resultDataJSON = json_encode($resultData);

echo $resultDataJSON;

#now appinventor's TinyWebDB1.GotValue, valuefromWEBDB will have the author's name 
//echo $xml;

#$resultData = array("VALUE","tag",array('peter'));
#["VALUE","author",["peter"]]
#$resultDataJSON = json_encode($resultData);


#echo $resultDataJSON;
#["VALUE","tag","peter"]
#["VALUE","\"tag\"","peter "]
#value <br of type java.lang.string cannot be converted to jsonarray
#echo json_encode("hello");


#["VALUE", "contacts", ["Lewis Moten", "John Smith", "Jane Doe"]]
#["VALUE","author",["Decker, Rick"]]
?>

