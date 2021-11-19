var variable_height = ($("#main-image-postcommentform").height() - $("#header-create-comment").outerHeight() - $("#submit-comment").outerHeight() - $("#like-create-comment").outerHeight() - 8);
$("#comment-section").css("height", variable_height.toString() + "px");


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
    $("#seeMarkedPosts").addClass("d-none");
    
    $("#buttonSeePosts").addClass("border-saved-or-posts");
    $("#buttonSeeSavedPosts").removeClass("border-saved-or-posts");
    $("#buttonSeeMarkedPosts").removeClass("border-saved-or-posts");

    $("#buttonMobilePosts").addClass("fontawesome-border-blue");
    $("#buttonMobileSavedPosts").removeClass("fontawesome-border-blue");
    $("#buttonMobileMarkedPosts").removeClass("fontawesome-border-blue");
    
}

function seeSavedPosts() {
    $("#seeSavedPosts").removeClass("d-none");
    $("#seePosts").addClass("d-none");
    $("#seeMarkedPosts").addClass("d-none");

    $("#buttonSeeSavedPosts").addClass("border-saved-or-posts");
    $("#buttonSeePosts").removeClass("border-saved-or-posts");
    $("#buttonSeeMarkedPosts").removeClass("border-saved-or-posts");
    
    $("#buttonMobileSavedPosts").addClass("fontawesome-border-blue");
    $("#buttonMobilePosts").removeClass("fontawesome-border-blue");
    $("#buttonMobileMarkedPosts").removeClass("fontawesome-border-blue");

}

function seeMarkedPosts() {
    $("#seeMarkedPosts").removeClass("d-none");
    $("#seePosts").addClass("d-none");
    $("#seeSavedPosts").addClass("d-none");

    $("#buttonSeeMarkedPosts").addClass("border-saved-or-posts");
    $("#buttonSeePosts").removeClass("border-saved-or-posts");
    $("#buttonSeeSavedPosts").removeClass("border-saved-or-posts");
    
    $("#buttonMobileMarkedPosts").addClass("fontawesome-border-blue");
    $("#buttonMobileSavedPosts").removeClass("fontawesome-border-blue");
    $("#buttonMobilePosts").removeClass("fontawesome-border-blue");
}

function goToSavedPosts() {
  window.location.href ="http://127.0.0.1:8000/insta/user/profilpage#execute";
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

$('.carousel').carousel({
 pause: false 
}) 

function goToStories(username) {
    var first_story_by_user = document.getElementsByClassName(username)[0];
    $('#carouselExampleIndicators').carousel(parseInt(first_story_by_user.id));
}

$("#pictureStory").hide();
$('#uploadButton').on('click', function () {
    $('#pictureStory').click();
});

$('#pictureStory').change(function () {
    var file = this.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        $('#pf-foto').css('background-image', 'url("' + reader.result + '")');
    }
    if (file) {
        reader.readAsDataURL(file);
    } else {
    }
});

function textAreaAdjust(element) {
    element.style.height = "1px";
    element.style.height = (element.scrollHeight - 6)+"px";
}

var width_textarea = $("#create-comment-mobile-form").width() - $(".table-cell-wrap>input").width();
$("#textarea-mobile-createcomment").css("width", width_textarea.toString()+"px");
$("#table-cell-wrap-textarea").css("width", width_textarea.toString()+"px");

var height_navbar = $("nav").outerHeight();
var height_createcomment = $(".bg-createcomment-mobile").outerHeight();
$("#commentsection-createcomment-mobile").css("top", (height_navbar + height_createcomment).toString() + "px");

$('#textarea-mobile-createcomment').on('input paste keyup change', function() {
    var height_navbar = $("nav").outerHeight();
    var height_createcomment = $(".bg-createcomment-mobile").outerHeight();
    $("#commentsection-createcomment-mobile").css("top", (height_navbar + height_createcomment).toString() + "px");
});

var original_text;
$('.show-child-comments').on('click', function(evt) {
    var sibling_section = $(this).next("section");
    children_span = $(this).children("span");
    var has_d_none_class = sibling_section.hasClass("d-none"); 
    if(has_d_none_class) {
        original_text = children_span.text();
        children_span.text("Antworten verbergen");
        sibling_section.removeClass("d-none");
    } else {
        sibling_section.addClass("d-none");
        children_span.text(original_text);
    }
}); 

$('.write-to-modal-textarea').on('click', function(evt) {
    var name = $(this).attr("name");
    var textarea = $(this).closest(".wrap-parent-and-child").find("div[id^='answerToParentComment']").find("textarea");
    //alert($(this).closest(".wrap-parent-and-child").find("div[id^='answerToParentComment']").find("textarea").attr("class"));
    textarea.val("@"+name);

}); 
