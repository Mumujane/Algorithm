<?php
/**
 * 快速排序
 * @author JaneMu <[<zengjane052@gmail.com>]>
 */
function qs($a, $s=0, $e=null){
    if(count($a) <= 1){
        return $a;
    }
    $middle = $a[0];

    $left = array();
    $right = array();

    for($i=1; $i<count($a); $i++){
        if($middle < $a[$i]){
            $right[] = $a[$i];
        }else{
            $left[] = $a[$i];
        }
    }


    $left = qs($left);
    $right = qs($right);

    return array_merge($left, array($middle), $right);
}

$a = array(22,22,13,421,4,56,3,67,365,87665,54,68,31);
print_r(qs($a));