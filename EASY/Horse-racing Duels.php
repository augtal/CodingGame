<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%d", $N);
$horses = array();
for ($i = 0; $i < $N; $i++)
{
    fscanf(STDIN, "%d", $pi);
    array_push($horses, $pi);
}

sort($horses);
$min = $horses[count($horses)-1];

for ($i = 1; $i < count($horses); $i++)
{
    $value = $horses[$i] - $horses[$i-1];
    if($value < $min)
    {
        $min = $value;
    }
}

echo($min);
// Write an answer using echo(). DON'T FORGET THE TRAILING \n
// To debug: error_log(var_export($var, true)); (equivalent to var_dump)
?>