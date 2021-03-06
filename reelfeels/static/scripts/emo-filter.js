$(".emo-filter").change(function(event){
  var checkbox = event.target;
  var label_id = $(this).attr('id');
  var label = $("label[for='"+label_id+"']");

  $(".filter-btn-container .nav-item .btn").each(function(){
    $(this).removeClass('active');
  });
  $(this).parent().addClass('active');

  //hides all videos that are not the selected emotion
  $(".video-container").each(function(){
    if (!$(this).hasClass(label.text().toLowerCase())) $(this).hide();
    else $(this).show();
  });
});
