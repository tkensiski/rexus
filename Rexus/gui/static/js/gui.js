$(document).ready( function() {
  $('#menu ul li a').on( 'click', function() {
  if ( $(this).parent().hasClass('active') ) {
    $(this).parent('li').removeClass('active');
  } else {
    $(this).parent('li').addClass('active');
  }
    return false;
  });


  $('#splash').on('click', function() {
    $(this).css('display','none');
  });

  $('.pager span').on('click', function(){
      $('.pager span').removeClass('active');
      $(this).addClass('active');
  });
  
  $('.close_menu').on('click', function(){
      $('#menu').css('margin-left','-21%');
      $('#overview').css('max-width','93%');
      $(this).css('display','none');
      $('.open_menu').css('display','block');
  });
  $('.open_menu').on('click', function(){
      $('#menu').css('margin-left','0');
      $('#overview').css('max-width','75%');
      $(this).css('display','none');
      $('.close_menu').css('display','block');
  });


  $('#grow_menu_page').on('click', function(){
    $('#grow_menu').css('display','block');
    $('#data_menu').css('display','none');
    $('#settings_menu').css('display','none');
  });
  $('#data_menu_page').on('click', function(){
    $('#data_menu').css('display','block');
    $('#grow_menu').css('display','none');
    $('#settings_menu').css('display','none');
  });
  $('#settings_menu_page').on('click', function(){
    $('#settings_menu').css('display','block');
    $('#data_menu').css('display','none');
    $('#grow_menu').css('display','none');
  });
});