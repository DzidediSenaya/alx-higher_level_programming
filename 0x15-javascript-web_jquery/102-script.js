$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>'); // Create a new <li> element
    $('.my_list').append(newItem);      // Append it to the <ul> element with class 'my_list'
  });

  $('#remove_item').click(function () {
    const listItems = $('.my_list li'); // Select all <li> elements in the list
    if (listItems.length > 0) {
      listItems.last().remove(); // Remove the last <li> element from the list
    }
  });

  $('#clear_list').click(function () {
    $('.my_list').empty(); // Remove all elements from the <ul> with class 'my_list'
  });
});

