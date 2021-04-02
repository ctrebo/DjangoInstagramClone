var variable_height = ($("#row-create-comment").height() - $("#header-create-comment").outerHeight() - $("#submit-comment").outerHeight() - 7);
$("#comment-section").css("height", variable_height.toString() + "px");

// var height = document.getElementById("#row-create-comment").height() -   


$( ".fontawesome-border" ).click(function() {
    $(this).css("text-shadow", "-1px 0 rgb(136, 128, 128), 0 1px rgb(136, 128, 128), 1px 0 rgb(136, 128, 128), 0 -1px rgb(136, 128, 128)")
  });

function copyToClipboard(mydata) {
    // var mydata = JSON.parse(document.getElementById('mydata').textContent);
    navigator.clipboard.writeText(mydata);

}
