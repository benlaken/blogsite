function main() {
  $('.select_item').mouseover(function(){
    $(this).addClass('hover_select');
  });
  $('.select_item').mouseout(function(){
    $(this).removeClass('hover_select');
  });
  $('.post-category').mouseover(function(){
    $(this).addClass('post-category_select');
  });
  $('.post-category').mouseout(function(){
    $(this).removeClass('post-category_select');
  });
};

$(document).ready(main);
