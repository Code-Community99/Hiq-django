$(document).ready(function(){
  $(".login").submit(function(event){
    event.preventDefault();
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    // console.log(email + password);
    window.location.href = "user.html";
  });
  // $(".signupForm").submit(function(event){
  //   event.preventDefault();
  //   var password = document.getElementById("password").value;
  //   var confirmPassword = document.getElementById("cpassword").value;
  //   alert(password + confirmPassword);
  //   window.location.href = "user.html";
  // });
  $(".ham").click(function() {
   $(".options").slideToggle();
   $(".nav").css("opacity", "1");
  });
  $(".hide").click(function() {
   $(".ev").slideToggle();
  });
  $(".backFlip").click(function(){
    $(".content").toggle();
    $(".backContent").toggle();
  });
  $(".Front").click(function(){
    $(".content").toggle();
    $(".backContent").toggle();
  });
  $(".close").click(function(){
    $(".ff").slideUp();
    $(".form").slideUp();
    $(".content").toggle();
    $(".backContent").toggle();
  });
  $("#showForm").click(function(){
    showform();
  });
  function showform() {
    $(".ff").show();
    $(".form").slideDown();
  }
  $(window).scroll(function(){
    if ($(document).scrollTop() > 50) {
            $(".nav").css("opacity", "0.6");
          } else {
            $(".nav").css("opacity", "1");
          }
})
$(window).scroll(function(){
  if ($(document).scrollTop() > 50) {
          $(".add-feed-section").slideUp();
        } else {
          $(".add-feed-section").slideDown();
        }
})

});
