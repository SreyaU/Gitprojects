// Basic interactive behaviours: smooth scrolling, resume download (simulated), contact form handling
document.addEventListener('DOMContentLoaded', function(){
  // smooth scroll for in-page links
  document.querySelectorAll('.nav a, .btn[href^="#"]').forEach(function(link){
    link.addEventListener('click', function(e){
      var href = this.getAttribute('href');
      if(href && href.startsWith('#')){
        e.preventDefault();
        var el = document.querySelector(href);
        if(el) el.scrollIntoView({behavior:'smooth',block:'start'});
      }
    });
  });

  // Download resume: generate a simple text resume file and trigger download
  var dl = document.getElementById('downloadResume');
  dl.addEventListener('click', function(e){
    e.preventDefault();
    var content = 'Browny Star - Resume\nUI/UX Designer & Web Developer\nEmail: browny@gmail.com\nPhone: 123-456-7890';
    var blob = new Blob([content], {type: 'text/plain'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'Browny_Star_Resume.txt';
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  });
});

// Simple contact form handler (no backend)
function handleContact(e){
  e.preventDefault();
  var form = e.target;
  var name = form.name.value.trim();
  var email = form.email.value.trim();
  var message = form.message.value.trim();
  if(!name || !email || !message){ alert('Please fill all fields'); return; }
  alert('Message sent (simulated) — ' + name);
  form.reset();
}
