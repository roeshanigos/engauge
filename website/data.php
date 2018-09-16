<?php
    $keyword = $_GET["keyword"];
    $info = $_GET["data"];
    
    $parts = explode("], [", $info);
    
    
    file_put_contents("keywords/" . $keyword . ".txt", "");
    
    foreach($parts as $part) {
        $part = str_replace( '[', '', $part );
        $part = str_replace( ']', '', $part );
        $part = str_replace( ',', '', $part );
        echo $part;
        file_put_contents("keywords/" . $keyword . ".txt", $part.PHP_EOL , FILE_APPEND | LOCK_EX);
    }
    
?>