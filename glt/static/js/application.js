$(document).ready(function(){
  console.log('?');
  $("form.insert-sibling-node").each(function(){
    var form = $(this);
    $(this).submit(function(e){
      e.preventDefault();
      alert(form.tagName);
/*
      var input = $("input[name='description']", form);
      alert('3:' + input.tagName);
      alert('Length: ' + input.value().length());
      return false;
      if (input.value().length() == 0)
        alert('Boo!');
*/
    });
  });
});

