<?php 
// var_dump(empty(""));
// var_dump(empty(0));
// var_dump(empty('0'));
// var_dump(empty(NULL));
// var_dump(empty(array()));

// $var;
// var_dump(isset($var));

// $test = 'aaaaa';
// $abc = &$test;
// unset($abc);
// var_dump($test);
// 
// 
$a="ABC";
$b =&$a;
var_dump($a);//这里输出:ABC
var_dump($b);//这里输出:ABC
$b="EFG";
unset($b);
var_dump($a);//这里$a的值变为EFG 所以输出EFG
var_dump($b);//这里输出EFG


$t = 10;
var_dump($t++);


var_dump(++$t);