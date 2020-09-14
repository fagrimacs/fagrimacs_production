// Call hideShow when page is loaded
$(document).ready(function(){
    hideShow()
});

// call hideShow when the user clicks on the component_type dropdownlist
$('#id_type').click(function(){
    hideShow()
});

// The jquery function below hides/shows the k_v, DI and length fields depending on the selected component_type 
function hideShow(){
    if(document.getElementById('id_type').options[document.getElementById('id_type').selectedIndex].value == "tractor")
    {
        $('#implement').hide();
        $('#tractor').show();
    } else if(document.getElementById('id_type').options[document.getElementById('id_type').selectedIndex].value == "implement")
    {
        $('#implement').show();
        $('#tractor').hide();
    } else {
        $('#tractor').hide();
        $('#implement').hide(); 
    }
}

// var x = document.getElementById("equipment").required;