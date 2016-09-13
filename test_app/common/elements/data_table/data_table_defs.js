
function applyRowIds($table) {
    var $rows = $table.find("tbody tr");
    $rows.each(function(i, val){
        var idx = i + 1;
        $(val).attr("id", "row_"+ idx)
    })

};

function applyRowBackground($table){
    var odd_color = "#ffffff";
    var even_color = "#f2f2f2";
    $table.find("tbody tr.odd").each(function() {
        $(this).css("background-color", odd_color)
    });
    $table.find("tbody tr.even").each(function() {
        $(this).css("background-color", even_color)
    });
};



function initDataTable($table, config) {


    var options = {};
    $.each(config, function(key, value){
        options[key] = value
    });

    $table.DataTable(options)

}


