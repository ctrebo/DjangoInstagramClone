$(".like_post_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    var this_form = $(this)
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var new_num_likes = JSON.parse(response["new_num_likes"]);
            var heart_tobe_red = JSON.parse(response["heart_tobe_red"]);
            var fa_heart_button = this_form.find('.fa-heart');
            var post_id = JSON.parse(response["post_id"]);
            var selector_like_field = "likenumber-" + post_id;
            var like_field = $("#" + selector_like_field);
            if(heart_tobe_red) {
                if(fa_heart_button.hasClass("text-white")) {
                    fa_heart_button.removeClass("text-white");
                }
                if(fa_heart_button.hasClass("fontawesome-border")) {
                    fa_heart_button.removeClass("fontawesome-border");
                }
                fa_heart_button.addClass("text-danger");

            } else {
                if(fa_heart_button.hasClass("text-danger")) {
                     fa_heart_button.removeClass("text-danger");
                }
                fa_heart_button.addClass("text-white fontawesome-border");
            }
            if(new_num_likes != 1) {
                like_field.html(new_num_likes + " Likes");
            } else {
                like_field.html("1 Like");
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".save_post_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    var this_form = $(this)
    // make POST ajax call
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var fa_bookmark_button = this_form.find('.fa-bookmark');
            var is_post_saved = JSON.parse(response["is_post_saved"]);
            if(is_post_saved) {
                if(fa_bookmark_button.hasClass("text-white")) {
                    fa_bookmark_button.removeClass("text-white");
                }
                if(fa_bookmark_button.hasClass("fontawesome-border")) {
                    fa_bookmark_button.removeClass("fontawesome-border");
                }
                fa_bookmark_button.addClass("text-dark");

            } else {
                if(fa_bookmark_button.hasClass("text-dark")) {
                     fa_bookmark_button.removeClass("text-dark");
                }
                fa_bookmark_button.addClass("text-white fontawesome-border");
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".like_postcomment_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    //alert(this_form.data('url'));
    // make POST ajax call
    var serializedData = $(this).serialize();

    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var new_num_likes = JSON.parse(response["new_num_likes"]);
            var heart_tobe_red = JSON.parse(response["heart_tobe_red"]);
            var fa_heart_button = this_form.find('.fa-heart');
            var postcomment_id = JSON.parse(response["postcomment_id"]);
            var selector_like_field = "likesComment-" + postcomment_id;
            var like_field = $("#" + selector_like_field);
            if(heart_tobe_red) {
                if(fa_heart_button.hasClass("text-white")) {
                    fa_heart_button.removeClass("text-white");
                }
                if(fa_heart_button.hasClass("fontawesome-border")) {
                    fa_heart_button.removeClass("fontawesome-border");
                }
                fa_heart_button.addClass("text-danger");

            } else {
                if(fa_heart_button.hasClass("text-danger")) {
                     fa_heart_button.removeClass("text-danger");
                }
                fa_heart_button.addClass("text-white fontawesome-border");
            }
            if(new_num_likes != 1) {
                like_field.html(new_num_likes + " Likes");
            } else {
                like_field.html("1 Like");
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".delete_postcomment_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();

    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var comment_id = JSON.parse(response["comment_id"]);
            var had_childs = JSON.parse(response["had_childs"]);
            comment_section_selector = "#comment-"+ comment_id;
            if(had_childs) {
                $(comment_section_selector).next(".show-child-comments").remove();
                $(comment_section_selector).next("section").addClass("d-none");
            }
            $("#modal-comment-" + comment_id).modal("hide");
            $('body').removeClass('modal-open');
            $('.modal-backdrop').remove();
            $(comment_section_selector).remove();
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".follow_user_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var is_following_now = JSON.parse(response["is_following_now"]);
            var is_not_following_now = JSON.parse(response["is_not_following_now"]);
            var is_requesting_now = JSON.parse(response["is_requesting_now"]);
            var usertofollow_is_private = JSON.parse(response["usertofollow_is_private"]);

            follow_button = this_form.find("button");
            follow_button.removeClass();
            if(is_following_now) {
                follow_button.addClass("btn bg-white border");
                follow_button.html("Unfollow")
            } else if(is_not_following_now && usertofollow_is_private) {
                follow_button.addClass("btn bg-primary border text-white");
                follow_button.html("Follow");
                
                $(".ajax_form_hide").remove();
                $(".ajax_form_show").removeClass("d-none");
                $(".ajax_form_show").addClass("d-block");
                    
            } else if(is_not_following_now && !usertofollow_is_private) { // Write all conditions out because of readability
                follow_button.addClass("btn bg-primary border text-white");
                follow_button.html("Follow");
            } else if(is_requesting_now) {
                follow_button.addClass("btn bg-white border");
                follow_button.html("Requested");
            }
             
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});


$(".follow_user_form_buttons").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var is_following_now = JSON.parse(response["is_following_now"]);
            var is_not_following_now = JSON.parse(response["is_not_following_now"]);
            var is_requesting_now = JSON.parse(response["is_requesting_now"]);
            var usertofollow_is_private = JSON.parse(response["usertofollow_is_private"]);

            follow_button = this_form.find("button");
            follow_button.removeClass();
            if(is_following_now) {
                follow_button.addClass("btn bg-white border");
                follow_button.html("Following")
            } else if(is_not_following_now) { // Write all conditions out because of readability
                follow_button.addClass("btn bg-primary border text-white");
                follow_button.html("Follow");
            } else if(is_requesting_now) {
                follow_button.addClass("btn bg-white border");
                follow_button.html("Requested");
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".follow_user_form_recommendations").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var is_following_now = JSON.parse(response["is_following_now"]);
            var is_not_following_now = JSON.parse(response["is_not_following_now"]);
            var is_requesting_now = JSON.parse(response["is_requesting_now"]);
            var usertofollow_is_private = JSON.parse(response["usertofollow_is_private"]);

            follow_button = this_form.find("button");
            follow_button.removeClass();
            if(is_following_now) {
                follow_button.addClass("border-0 bg-transparent text-dark");
                follow_button.html("Following")
            } else if(is_not_following_now) { // Write all conditions out because of readability
                follow_button.addClass("border-0 bg-transparent text-info");
                follow_button.html("Follow");
            } else if(is_requesting_now) {
                follow_button.addClass("border-0 bg-transparent text-dark");
                follow_button.html("Requested");
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".follow_hashtag_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            var follows_now = JSON.parse(response["follows_now"]);

            follow_button = this_form.find("button");
            follow_button.removeClass();
            if(follows_now) {
                follow_button.addClass("btn bg-white border text-dark");
                follow_button.html("Following")
            } else { 
                follow_button.addClass("btn bg-primary border text-white");
                follow_button.html("Follow")
            }
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});

$(".accept_or_delete_form").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var this_form = $(this)
    // make POST ajax call
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: this_form.data('url'),
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            this_form.closest(".userwhorequested-section").remove();
        },
        error: function (response) {
            // alert the error if any error occured
            alert("Error");
        }
    })
});
