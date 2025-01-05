// SPDX-License-Identifier: MIT



pragma solidity ^0.8.26;

contract calculator{

    
    uint256 result=0;

    function add(uint256 num1,uint256 num2) public {

         result = num1+num2;
         
    }
    
   

    function subtract(uint256 num1,uint256 num2) public {

         
         result = num1-num2;
         
    }

     function multiply(uint256 num1,uint256 num2) public {

         
         result = num1*num2;
         
    }

    function divide(uint256 num1,uint256 num2) public {

         
         result = num1/num2;
         
    }
    
    function get() public view returns  (uint256) {
         return result; 
    }


}

