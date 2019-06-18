<?php

class Solution {

    /**
     * @param Float $x
     * @param Integer $n
     * @return Float
     */
    function myPow($x, $n) {
        if(!$n){
            return 1;
        }
        if ($n <= 0) {
            return 1/self::myPow($x, -$n);
        }
        if ($n %2) {
            return $x * self::myPow($x, $n-1);
        }

        return self::myPow($x*$x, $n/2);
    }
}

$solituon = Solution::myPow(2, 5);
print_r($solituon);