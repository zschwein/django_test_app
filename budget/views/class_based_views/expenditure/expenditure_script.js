/**
 * Created by zschweinfurth on 11/15/2015.
 */

var csrftoken = Cookies.get("csrftoken");

function initDatePicker() {
   $(".datepicker").each(function()
   {        $(this).datepicker({
            showOptions: {direction: "up"},
            changeYear: true,
            changeMonth: true,
            autoSize: true,
            dateFormat: "yy-mm-dd",
            showAnim: "fade"
        });
    })
}

function initDataTable() {
    var $exp_table = $("#expenditure_table");
    $exp_table.DataTable(
        {
            "drawCallback": function( settings ) {initDatePicker();}
        });
}


function initDataTable2() {
    var $table = $("#test_table");
    $table.DataTable(
        {
            "ajax": '/budget?exp_json=true',
        });
}


function form_table_first_row($object){
    var $table = $object.DataTable();
    return $($table.row( 0 ).node())
}

function form_table_add_row($object, row){
    var $table = $object.DataTable();
    $table.row.add(row).draw();
}

function seralize_form_data_rows($object) {
        var $rows = $object.find('tbody tr');
        var $row_val = $rows.map(function() {return $(this).find("input, select");});
        var json_array = [];
        $row_val.each(function() {json_array.push($(this).serializeArray())});
        return JSON.stringify(json_array);
}


//function to define csrf safe methods
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function validate_all_inputs_filled($table) {
    var $inputs = $table.find("tbody td :input");
    var warns = 0;
    $inputs.map(function () {
        if (!$(this).val()) {
            warns++;
            $(this).addClass('warning');
        } else if ($(this).val()) {
            $(this).removeClass('warning');
        }
    });
    return warns
}


function exp_from_ajax_post(){
    $.ajax({
        type: "POST",
        data: {'data': seralize_form_data_rows($("#expenditure_table"))},

        // django set csrf token header
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },

         success : function(json) {
             //clear form data table
             var $exp_table = $("#expenditure_table");
             var $rows = $exp_table.find("tbody tr");
             var to_go = $rows.splice(1, $rows.length);
             var $exp_dt = $exp_table.DataTable();
             $exp_dt.rows(to_go).remove();
             $exp_dt.draw();
             var $ins = $exp_table.find(":input");
             $ins.each(function(){
                $(this).val('')
             });
             //reload list view of exps
             $("#test_table").DataTable().ajax.reload();
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        error: function() {console.log("no")}

    });
}





$(document).ready(function() {
    initDataTable();
    var $exp_table = $("#expenditure_table");

    initDataTable2();


    //add row to expenditure table click handler
    var cloneCount = 1;
    $("#addRow").on("click", function(event) {
        event.preventDefault();
        var warns = validate_all_inputs_filled($exp_table);
        if(warns > 0) {
            alert('All fields required')
        } else {
        //var $exp_table = $("#expenditure_table");
        var $row_node = form_table_first_row($exp_table);
        var $to_be_row = $row_node.find("input, select").each(function() {
            if ($(this).attr("name") === "Date") {
                $(this).attr("class", "datepicker")
            }
        });
        var to_be_string_array = $to_be_row.map(function()
        {
            var $base = $(this).clone();
            var id_text = $base.attr('id');
            return $base.attr('id', id_text+cloneCount++).wrap('<p>').parent().html();
        }).toArray();
        form_table_add_row($exp_table, to_be_string_array);
    }});

    //event handlers
    //expense form submit event handler

    $("#exp_form_submit").on("click", function(event){
        event.preventDefault();
        warns = validate_all_inputs_filled($exp_table);
        if(warns > 0) {
            alert('All Fields Required')
        } else {
            alert('you submit...');
            //call to ajax to submit data
            exp_from_ajax_post();
        }
    });


    $("#id_ExpenseTypeName").keypress(function(event) {

        //if key is enter key
        if(event.which == 13) {
            event.preventDefault();
            alert("You pressed enter on my form");
        }
    });

});