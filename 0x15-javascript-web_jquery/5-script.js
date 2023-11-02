$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>'); // Create a new <li> element
    $('.my_list').append(newItem);      // Append it to the <ul> element with class 'my_list'
  });
});

