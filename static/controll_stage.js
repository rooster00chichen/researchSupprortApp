function change_status_message(is_op) {
  // 現在情報をHTMLに出力
  if (is_op == 'True') {
    change_status_message_abled()
  } else if (is_op == "False") {
    change_status_message_disabled()
  } else {
    status_text.textContent = "now:cant cheak";
  }
}

function change_status_message_abled() {
  const status_text = document.getElementById('status');
  const status_button = document.getElementsByClassName('button-status-color');
  status_text.textContent = `now:can operate`;
  for (const one_button of status_button) {
    one_button.disabled = null;
    one_button.style.color = "#2589d0";
    one_button.style.border = "1px solid #2589d0";
  }
}

function change_status_message_disabled() {
  const status_text = document.getElementById('status');
  const status_button = document.getElementsByClassName('button-status-color');
  status_text.textContent = `now:cant operate`;
  for (const one_button of status_button) {
    one_button.disabled = 'disabled';
    one_button.style.color = "#c8c8c8";
    one_button.style.border = "1px solid #c8c8c8";
  }
}