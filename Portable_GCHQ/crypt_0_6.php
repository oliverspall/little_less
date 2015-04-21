<!doctype html>
<html>
<head>
<title>Encrypt</title>
</head>

<body>

<?php
	$myfile = fopen("fbdownloadall200115.txt", "r") or die("Unable to open file...");
	echo fread($myfile,filesize("fbdownloadall200115.txt"));
	fclose($myfile);
	echo "this is the text to be encrypted...";

	$iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_256, MCRYPT_MODE_ECB);
	$iv = mcrypt_create_iv($iv_size, MCRYPT_RAND);
	$key = "facebookdataisfreetouse";
	$text = file_get_contents('fbdownloadall200115.txt');
	echo strlen($text) . "\n";

	$crypttext = mcrypt_encrypt(MCRYPT_RIJNDAEL_256, $key, $text, MCRYPT_MODE_ECB, $iv);
	file_put_contents('/Users/oliverspall/Dropbox/Work/Gold/Practical Methods/Minor project/Encryption/encrypted_fb200115.txt', $crypttext);

	/* Terminate encryption handler */
	mcrypt_generic_deinit($td);

	echo $crypttext;

?>

</body>
</html>