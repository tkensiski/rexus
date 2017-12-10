$(document).ready( function() {
  $('#menu ul li a').on( 'click', function() {
  if ( $(this).parent().hasClass('active') ) {
    $(this).parent('li').removeClass('active');
  } else {
    $(this).parent('li').addClass('active');
  }
  return false;
});

  $('.pager span').on('click', function(){
      $('.pager span').removeClass('active');
      $(this).addClass('active');
  });
  
  $('.close_menu').on('click', function(){
      $('#menu').css('margin-left','-17%');
      $(this).css('display','none');
      $('.open_menu').css('display','block');
  })
  $('.open_menu').on('click', function(){
      $('#menu').css('margin-left','0');
      $(this).css('display','none');
      $('.close_menu').css('display','block');
  })
});