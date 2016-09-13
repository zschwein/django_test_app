/**
 * Created by zschweinfurth on 11/11/2015.
 */

function turn_blue($obj)

{
    $obj.css("color:blue")
}


$(document).ready(function()

{
    $("p").each(function(){
        turn_blue(this)
    })


})