const tableMonth = document.querySelector('tr:first-child th:first-child');
const tableDates = document.querySelectorAll('td');
const eventUls = document.querySelectorAll('.events ul');
const monthNames = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
};

tableDates.forEach((tableDate) => {
    if (tableDate.textContent.trim() === '') {
        tableDate.classList.add('empty-cell');
    }

    const aTag = document.createElement('a');
    aTag.href = '#';
    aTag.textContent = tableDate.textContent;

    const clickedNum = tableDate.textContent;
    const [month, year] = tableMonth.textContent.split(' ');
    const clickedDate = `${month} ${clickedNum}, ${year}`;
    const today = new Date();
    const todayDate = today.getDate();
    const todayMonth = today.getMonth() + 1;
    const todayYear = today.getFullYear();

    for (const monthName in monthNames) {
        if (monthNames.hasOwnProperty(monthName)) {
            if (monthName == month) {
                if (clickedNum == todayDate && monthNames[month] == todayMonth && year == todayYear) {
                    tableDate.style.backgroundColor = 'lightsalmon';
                }
            }
        }
    }

    eventUls.forEach((eventUl) => {
        const ulDate = eventUl.dataset.date;
        const eventUlMonth = ulDate.split(' ')[0];
        const eventUlDate = ulDate.split(' ')[1].replace(',', '');
        const eventUlYear = ulDate.split(' ')[2];

        if (tableDate.textContent == eventUlDate && month == eventUlMonth && year == eventUlYear) {
            aTag.style.backgroundColor = 'lightseagreen';
        }
    
        aTag.addEventListener('click', (e) => {
            e.preventDefault();
            eventUl.style.display = 'none';
            
            if (ulDate === clickedDate && eventUl.style.display == 'none') {
                eventUl.style.display = 'grid';
            } else {
                eventUl.style.display = 'none';
            }
        });
    });

    tableDate.innerHTML = '';
    tableDate.appendChild(aTag);
});
