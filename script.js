document.getElementById("year").textContent = new Date().getFullYear();

function handleFormSubmit(event) {
  event.preventDefault();
  
  const form = event.target;
  const formData = new FormData(form);
  const name = formData.get('name');
  const email = formData.get('email');
  const company = formData.get('company');
  const areas = formData.getAll('area');
  
  if (areas.length === 0) {
    alert('Kérlek válassz legalább egy területet!');
    return;
  }

  // Email összeállítása
  const subject = encodeURIComponent('Új kapcsolatfelvétel: ' + company.substring(0, 50));
  const body = encodeURIComponent(
    'Név: ' + name + '\n' +
    'E-mail: ' + email + '\n' +
    'Cég / Projekt: ' + company + '\n' +
    'Érdeklődési terület: ' + areas.join(', ')
  );
  
  // Mailto link megnyitása
  window.location.href = 'mailto:hello@bognar.dev?subject=' + subject + '&body=' + body;
  
  // Form reset
  form.reset();
  
  // Visszajelzés
  alert('Köszönjük! Az e-mail kliens megnyílik. Ha nem, írj közvetlenül a hello@bognar.dev címre.');
}
