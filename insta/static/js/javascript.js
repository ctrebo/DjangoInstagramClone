var variable_height = ($("#row-create-comment").height() - $("#header-create-comment").outerHeight() - $("#submit-comment").outerHeight() - $("#like-create-comment").outerHeight() - 8);
$("#comment-section").css("height", variable_height.toString() + "px");

$("#like-create-comment").css("bottom", ($("#submit-comment").outerHeight() + 7).toString() + "px");
$("#save-create-comment").css("bottom", ($("#submit-comment").outerHeight() + 7).toString() + "px");


$( ".fontawesome-border" ).click(function() {
    $(this).css("text-shadow", "-1px 0 rgb(136, 128, 128), 0 1px rgb(136, 128, 128), 1px 0 rgb(136, 128, 128), 0 -1px rgb(136, 128, 128)")
  });

$("#searchfield-mobile").css("width", ($("body").outerWidth() - $("#ul-mobile-search").outerWidth() - 12).toString() + "px")


//add placeholder and padding to login form username
$("#id_username").attr("placeholder", "Username");
$("#id_username").css("padding-left", "0.25rem");
$("#id_username").css("padding-right", "0.25rem");
$("#id_username").css("border-radius", "3px");
$("#id_username").css("width", "100%");
//add placeholder and padding to login form password
$("#id_password").attr("placeholder", "Password");
$("#id_password").css("padding-left", "0.25rem");
$("#id_password").css("padding-right", "0.25rem");
$("#id_password").css("border-radius", "3px");
$("#id_password").css("width", "100%");

//variable to save time when prev function was clicked
var t0;
//variable that saves if currently there gets something copied and if slider is still open 
var copiedMessageInFrame = false;
//variable that saves if this is the first time something gets copied
var copiedAgain = false;
// var timeLastTimeFun;

function openAndCloseCopyMessage(mydata) {
    navigator.clipboard.writeText(mydata);
    $(".copy-link-slider").css("margin-bottom", "0px");
    // prevCopiedMessageInFrame = copiedMessageInFrame;
    copiedMessageInFrame = true;
    setTimeout(function () {
      if(!copiedAgain) {
      $(".copy-link-slider").css("margin-bottom", "-50px");
      copiedMessageInFrame = false;
    }  else {
      // timeLastTimeFun = Date.now();
      var t1 = performance.now()
      var minusTime = 5000 - (t1-t0-500);
      if(minusTime < 0 || (5000 - t1 - t0 > 5500)) {
        minusTime = 5000;
      }
      
      setTimeout(function() {
        $(".copy-link-slider").css("margin-bottom", "-50px");
      }, 5000 - minusTime);
      }  
    }, 5000);
}

function copyToClipboard(mydata) {
    if(copiedMessageInFrame == true){
      copiedAgain = true
      copiedMessageInFrame = false;
      $(".copy-link-slider").css("margin-bottom", "-50px");
      setTimeout(function () {
        openAndCloseCopyMessage(mydata);
      }, 500);
    }
    else {
      openAndCloseCopyMessage(mydata);
      t0 = performance.now()

    }
}


function seePosts() {
    $("#seePosts").removeClass("d-none");
    $("#seeSavedPosts").addClass("d-none");
    $("#buttonSeePosts").addClass("border-saved-or-posts");
    $("#buttonSeeSavedPosts").removeClass("border-saved-or-posts");

}

function seeSavedPosts() {
    $("#seeSavedPosts").removeClass("d-none");
    $("#seePosts").addClass("d-none");
    $("#buttonSeeSavedPosts").addClass("border-saved-or-posts");
    $("#buttonSeePosts").removeClass("border-saved-or-posts");
}

function goToSavedPosts() {
  window.location.href ="http://127.0.0.1:8000/insta/profilpage#execute";
}

if (window.location.hash === '#execute') {
  seeSavedPosts();
  history.replaceState(null, null, ' ');
  
}

$( ".single-comment" ).hover(
  function() {
    $( this ).children(".comment-options").removeClass("d-none");
  }, function() {
    $( this ).children(".comment-options").addClass("d-none");
  }
);