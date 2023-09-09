<?php
    $key = 'KNHL';
    $text = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
    $outText = "";

    for($i=0;$i<strlen($text);$i++) {
    	$outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    echo base64_encode($outText);
?>
