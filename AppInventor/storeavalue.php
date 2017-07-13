<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: text/json;");



#. for concatenation

#print_var for human readable data
#$_GET for the url parameters sent in post req

#for testing using $_GET
#http://192.168.1.16/setvalue?tag=isbn&value=9780131988132
#var_dump($_GET);

#FORMAT
# ["STORED", "firstName", "\"Lewis\""]

#get the tag and value from appinventor
$tag = $_POST['tag'];
$value = $_POST['value'];

#Need not store the who JSON in the file for the isbn number, just store the isbn number
#store in a file

#store only the isbn in the file
#store a value without quotes. APPInventor sends the isbn number with by default and the code will not work
#trim it, test with barcode and see if it sends with quotes
$value = trim($value,'"');

#write to the file
file_put_contents('isbnval.txt', $value);

#Store in session
#session_start();
#$_SESSION['isbndata'] = $retval;
?>

