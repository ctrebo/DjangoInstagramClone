var variable_height = ($("#row-create-comment").height() - $("#header-create-comment").outerHeight() - $("#submit-comment").outerHeight() - 7);
$("#comment-section").css("height", variable_height.toString() + "px");

// var height = document.getElementById("#row-create-comment").height() -   


$( ".fontawesome-border" ).click(function() {
    $(this).css("text-shadow", "-1px 0 rgb(136, 128, 128), 0 1px rgb(136, 128, 128), 1px 0 rgb(136, 128, 128), 0 -1px rgb(136, 128, 128)")
  });



var copiedMessageInFrame = false;

function openAndCloseCopyMessage(mydata) {
  navigator.clipboard.writeText(mydata);
  $(".copy-link-slider").css("margin-bottom", "0px");
  copiedMessageInFrame = true;
  setTimeout(function () {
    $(".copy-link-slider").css("margin-bottom", "-50px");
    copiedMessageInFrame = false; 
  }, 10000);
}

function copyToClipboard(mydata) {
    if(copiedMessageInFrame == true){
      copiedMessageInFrame = false;
      $(".copy-link-slider").css("margin-bottom", "-50px");
      setTimeout(function () {
        openAndCloseCopyMessage(mydata);
      }, 500);
    }
    else {
      openAndCloseCopyMessage(mydata);
    }

}
