<?php
$cookie_plain = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));

$cookie_encrypted = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D");

echo $cookie_plain ^ $cookie_encrypted;

?>
