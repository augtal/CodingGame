<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%s", $LON);
fscanf(STDIN, "%s", $LAT);
fscanf(STDIN, "%d", $N);

$LON = str_replace(',','.',$LON);
$LAT = str_replace(',','.',$LAT);

$defibs = array();

for ($i = 0; $i < $N; $i++)
{
    $D = stream_get_line(STDIN, 256 + 1, "\n");
    $D = str_replace(',','.',$D);
    array_push($defibs, explode(";",$D));
}

$min = PHP_INT_MAX;
$minIndex = -1;
for ($i=0; $i < $N; $i++) { 
    $longA = floatval($LON);
    $latA = floatval($LAT);

    $longB = floatval($defibs[$i][count($defibs[$i])-2]);
    $latB = floatval($defibs[$i][count($defibs[$i])-1]);
    
    $x = ($longB - $longA) * cos((($latA + $latB) / 2));
    $y = ($latB - $latA);

    $d = sqrt((pow($x, 2) + pow($y, 2))) * 6371;

    if ($d< $min)
    {
        $min = $d;
        $minIndex = $i;
    }
}

// Write an answer using echo(). DON'T FORGET THE TRAILING \n
// To debug: error_log(var_export($var, true)); (equivalent to var_dump)

echo($defibs[$minIndex][1] . "\n");
?>