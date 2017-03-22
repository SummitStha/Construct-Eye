/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: http://creative-tim.com
 * 
 */

$(function() {

function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });     
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
       
}
function showLoginForm(){
    $('#loginModal .registerBox').fadeOut('fast',function(){
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');    
        });
    
        $('.modal-title').html('Login with');
    });       
     $('.error').removeClass('alert alert-danger').html(''); 

}

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#loginModal").modal("show");
      },
      success: function (data) {
        $("#loginModal .modal-content").html(data.html_form);
      }
    });    
    }, 230);
    
}
function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#loginModal").modal("show");
      },
      success: function (data) {
        $("#loginModal .modal-content").html(data.html_form);
      }
    }); 
    }, 230);
    
}

function loginAjax(){
    /*   Remove this comments when moving to server
    $.post( "/login", function( data ) {
            if(data == 1){
                window.location.replace("/home");            
            } else {
                 shakeModal(); 
            }
        });
    */

/*   Simulate error message from the server   */
     shakeModal();
}

function shakeModal(){
    $('#loginModal .modal-dialog').addClass('shake');
             $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
             $('input[type="password"]').val('');
             setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 ); 
}

//loginform
var loginForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#main-menu a").html(data.html_user);
          $("#loginModal").modal("hide");
        }
        else {
          $("#loginModal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

//loginform
var SignForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".user a").html(data.html_user);
          $("#loginModal").modal("hide");
        }
        else {
          $("#loginModal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };
  var loadForm = function () {
    showLoginForm();
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-event").modal("show");
      },
      success: function (data) {
        $("#modal-event .modal-content").html(data.html_form);
      }
    });
  };
//load form
  $(".js-signup-loadForm").click(loadForm);

//lOGIN
 $("#loginModal").on("submit", ".js-user-login-form",loginForm ); 
   $(".js-login-loadForm").click(loadForm);
 
  $("#loginModal").on("submit", ".js-user-create-form", loginForm);

});
 // this is custom added js
