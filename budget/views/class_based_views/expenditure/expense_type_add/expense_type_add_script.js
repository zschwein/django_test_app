/**
 * Created by zschweinfurth on 1/10/2016.
 */
$(document).ready(function(){

    var $exp_type_dlg = $("#exp_type_dialog_div");

    //inialize dailog obect
    var $ned = $exp_type_dlg.dialog(
    {
        title: 'New Facility ECM',
        width: 1300,
        height: 630,
        autoOpen: false,
        modal: true,
        zIndex: 4999,
        position: {
            of: '#top_block_row',
            at: 'center'
        }
    });


});