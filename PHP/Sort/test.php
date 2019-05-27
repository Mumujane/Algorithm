<?php 
// var_dump(empty(""));
// var_dump(empty(0));
// var_dump(empty('0'));
// var_dump(empty(NULL));
// var_dump(empty(array()));
// $var;
// var_dump(isset($var));
// 
// 


var_dump(memory_get_usage());   //获取内存
$a = "laruence";                //定义一个变量
var_dump(memory_get_usage());   //定义变量之后获取内存
unset($a);                      //删除该变量
var_dump(memory_get_usage());   //删除变量后获取内存