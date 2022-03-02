window.addEventListener('load', function () {
    var variable_height = ($("#main-image-postcommentform").height() - $("#header-create-comment").outerHeight() - $("#submit-comment").outerHeight() - $("#like-create-comment").outerHeight() - $("#like-count").outerHeight() - 8);
    $("#comment-section").css("height", variable_height.toString() + "px");
})

$("#searchfield-mobile").css("width", ($("body").outerWidth() - $("#ul-mobile-search").outerWidth() - 12).toString() + "px");


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

function seeTopPosts() {
    $("#topPosts").removeClass("d-none");
    $("#mostRecentPosts").addClass("d-none");

    $("#buttonTopPosts").addClass("border-saved-or-posts");
    $("#buttonMostRecentPosts").removeClass("border-saved-or-posts");
}

function seeMostRecentPosts() {
    $("#mostRecentPosts").removeClass("d-none");
    $("#topPosts").addClass("d-none");

    $("#buttonMostRecentPosts").addClass("border-saved-or-posts");
    $("#buttonTopPosts").removeClass("border-saved-or-posts");
}

//////////////////////////////////////////////////////////////////////////

function seeUserFollowings() {
    $("#following_hashtag").addClass("d-none")
    $("#following_user").removeClass("d-none")

    $("#seeHashtagsFollowing").removeClass("user-and-hashtag-clicked")
    $("#seeUsersFollowing").addClass("user-and-hashtag-clicked")

}

function seeHashtagFollowings() {
    $("#following_hashtag").removeClass("d-none")
    $("#following_user").addClass("d-none")

    $("#seeHashtagsFollowing").addClass("user-and-hashtag-clicked")
    $("#seeUsersFollowing").removeClass("user-and-hashtag-clicked")
}

function seeUserFollowingsMobile() {
    $("#following_hashtag_mobile").addClass("d-none")
    $("#following_user_mobile").removeClass("d-none")
   //$("#following_hashtag_mobile").removeClass()

    
    $("#seeHashtagsFollowingMobile").removeClass("user-and-hashtag-clicked")
    $("#seeUsersFollowingMobile").addClass("user-and-hashtag-clicked")
}

function seeHashtagFollowingsMobile() {
    $("#following_hashtag_mobile").removeClass("d-none")
    $("#following_user_mobile").addClass("d-none")

    $("#seeHashtagsFollowingMobile").addClass("user-and-hashtag-clicked")
    $("#seeUsersFollowingMobile").removeClass("user-and-hashtag-clicked")
}

if (window.location.hash === '#execute') {
    seeSavedPosts();
    history.replaceState(null, null, ' ');
  
}

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

// If 'Answer' gets clicked write 'parent_id' into
// the input(to signal that it is a childcomment) and 
// write the the username of author as value of input
//$('.write-to-textarea').on('click', function(evt) {
//    // Tomorow find way to pass id of parent comment to input as value
//    var name_of_author = $(this).attr("name");
//    var parent_id = $(this).next().attr("name");
//    var form_textarea = $("#form-write-comment");
//    var textarea = form_textarea.find("textarea");
//    var input_child_comment = $("#parent_id");
//    input_child_comment.attr("name", "parent_id");
//    input_child_comment.attr("value", parent_id);
//
//    textarea.val("@"+name_of_author);
//
//}); 

$('.write-to-textarea').on('click', function(evt) {
    // Tomorow find way to pass id of parent comment to input as value
    var name_of_author = $(this).attr("name");
    var parent_id = $(this).next().attr("name");
    var form_textarea = $("#form-write-comment");
    var form_textarea_mobile = $("#create-comment-mobile-form");
    var textarea = form_textarea.find("textarea");
    var textarea_mobile = form_textarea_mobile.find("textarea");
    var input_child_comment = $("#parent_id");
    input_child_comment.attr("name", "parent_id");
    input_child_comment.attr("value", parent_id);

    textarea.val("@"+name_of_author + " ");
    textarea.focus();
    textarea_mobile.val("@"+name_of_author + " ");
    textarea_mobile.focus();
}); 

