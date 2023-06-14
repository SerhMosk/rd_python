let sendBtnColor = 'rgba(112,181,249,0.2)';
let sendBtnTextColor = '#0a66c2';

const getRndInteger = (min, max) => {
  return Math.floor(Math.random() * (max - min)) + min;
}

const getContactWord = (cnt) => {
    const lastSymbol = (cnt + '').charAt(cnt.length - 1);
    return '<span>' + cnt + '</span> контакт' + (lastSymbol === '1' ? '' : lastSymbol === '2' ? 'и' : 'ів');
}

const getBtnElem = (target) => target.tagName === 'I' ? target.parentElement : target;

const addFriendHandler = (event) => {
    const btn = getBtnElem(event.target);
    btn.setAttribute('disabled', 'disabled');
    btn.innerHTML = '<i class="bi bi-hourglass-split me-1"></i> Очікується підтвердження';

    const contactCnt = document.getElementById('contactCounter');
    const cnt = parseInt(document.querySelector('#contactCounter span').innerText) + 1;
    contactCnt.innerHTML = getContactWord(cnt);
}

const sendMsgHandler = (event) => {
    const btn = getBtnElem(event.target);
    const btnColor = btn.style.backgroundColor;
    const btnTextColor = btn.style.color;

    btn.style.backgroundColor = sendBtnColor;
    btn.style.color = sendBtnTextColor;
    sendBtnColor = btnColor;
    sendBtnTextColor = btnTextColor;
}

const offerJobHandler = (event) => {
    const addToFriendsBtn = document.getElementById('addToFriends');
    addToFriendsBtn.classList.toggle('d-none');
}

const submitHomeworkHandler = (event) => {
    const homeWorkTable = document.getElementById('homeWorkTable').children[1];
    const newRow = document.createElement('tr');

    const newRecord = [26, 'Базова робота з HTML/CSS', 1, 2, 7];
    let i = 0;
    newRecord.forEach(item => {
        const newCol = document.createElement(i === 0 ? 'th' : 'td');
        if (i === 0) {
            newCol.setAttribute('scope', 'row');
        }
        newCol.innerText = item;
        newRow.appendChild(newCol);
        i++;
    });

    homeWorkTable.appendChild(newRow);


    const btn = getBtnElem(event.target);
    btn.setAttribute('disabled', 'disabled');
    btn.classList.add('btn-success');
    btn.classList.remove('btn-primary');
    btn.innerHTML = '<i class="bi bi-check-square-fill me-1"></i> ДЗ здано';
}

window.onload = () => {
    const contactCnt = document.getElementById('contactCounter');
    contactCnt.innerHTML = getContactWord(getRndInteger(1, 500));

    const addToFriendsBtn = document.getElementById('addToFriends');
    const sendMessageBtn = document.getElementById('sendMessage');
    const jobOfferBtn = document.getElementById('jobOffer');
    const submitHomeworkBtn = document.getElementById('submitHomework');

    addToFriendsBtn.addEventListener('click', addFriendHandler);
    sendMessageBtn.addEventListener('click', sendMsgHandler);
    jobOfferBtn.addEventListener('click', offerJobHandler);
    submitHomeworkBtn.addEventListener('click', submitHomeworkHandler);
};

window.onclose = () => {
    const addToFriendsBtn = document.getElementById('addToFriends');
    const sendMessageBtn = document.getElementById('sendMessage');
    const jobOfferBtn = document.getElementById('jobOffer');
    const submitHomeworkBtn = document.getElementById('submitHomework');

    addToFriendsBtn.removeEventListener('click', addFriendHandler);
    sendMessageBtn.removeEventListener('click', sendMsgHandler);
    jobOfferBtn.removeEventListener('click', offerJobHandler);
    submitHomeworkBtn.addEventListener('click', submitHomeworkHandler);
}