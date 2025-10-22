function submitContact(e){
  e.preventDefault();
  var f = e.target;
  var name = f.name.value.trim();
  var email = f.email.value.trim();
  var message = f.message.value.trim();
  if(!name || !email || !message){
    alert('Please fill all fields');
    return;
  }
  console.info('Contact form submitted', {name:name, email:email});
  alert('Message received. I will respond by email.');
  f.reset();
}
document.addEventListener('keydown', function(e){
  if(e.key === 'Tab'){
    document.body.classList.add('show-focus-outlines');
  }
});
