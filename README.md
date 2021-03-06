(upd: 2.04.22) Добавлена первая версия игры для запуска скачайте "Запуск из exe" и стартуйте main.exe.

(upd: 2.04.22 ближе к ночи) Исправлены некоторые баги, добавлена возможность ввода с нумпада, игра больше
не вылетает после окончания, есть выбор уровня сложности.

(upd: 3.04.22) Исправлена возможность абуза(через ввод после окончания игры), добавлены все меню игры, 
добавлены звуки и музыка, добавлены сохранения рекордов и настроек включения звука (файл с настройками условно зашифрован).

(upd: 12.04.22) Добавлена возможность ввода клавишей ENTER с нумпада, исправлен баг с вылетом игры из-за нажатия ENTER два
раза подряд. Произведен рефакторинг кода, далее будут уже не большие изменения.

# Техническое задание для курсовой работы
## Постановка задачи
Необходимо разработать игру "Математические пузыри", в которой разноцветные пузыри с арифметическими примерами
будут падать с верху экрана в низ. Задача пользователя лопать пузыри, не давая им коснуться края экрана и 
попутно зарабатывая очки. Для того чтобы лопнуть пузырь, необходимо дать правильный ответ на пример, 
заключенный внутри него.
## Основные требования
* Приложение необходимо реализовать на языке Python 3.10 с использованием библиотеки Pygame;
* Пользовательский ввод должен быть реализован, как с клавиатуры, так и голосом через стандартный 
микрофон устройства;
* Должно быть реализовано три уровня сложности игры;
* Со временем нахождения в одной сессии скорость падения пузырей должна увеличиваться увеличивается;
* Также в игре должна быть реализована система сохранения рекордов и 
подсчетов результатов. 

## Недопустимые функции
В игре не должно быть:
* донат - системы, и других способов получения нечестного премущества;
* сетевой игры и соревновательной системы, за исключением той, которую пользователь может придумать сам для 
игры в компании друзей и соревнований в реальной жизни.

## Особенности игрового процесса
Реализация уровней сложности должна быть сделана за счет сложности арифметических примеров. Также на разных
уровнях сложности должен быть использован разный фон. Пузырьки обязательно должны лопаться со звуком. При 
записи нового рекорда должно быть поздравление для игрока. После проигрыша должна выводиться надпись: "Игра 
окончена", результат и количество очков необходимое для достижения рекорда. Цветовая палитра пузырей должна 
быть ограничена 10ю цветами. На экране в один момент не должно быть более 7 пузырей. Если результат введенный 
пользователем решает сразу несколько примеров, все шарики, для которых ответ верен, должны лопнуть. Поле ввода
находится вверху экрана по средине и занимает 4 знакоместа. В правом верхнем углу находится счетчик очков.

### Генерация пузырей 
Пузырь выглядит как эллипс 270х160px, цвет для каждого выбирается случайным образом из палитры. В зависимости 
от сложности игры, из набора математических операций выбирается одна, далее генерируется два числа и явно
вычисляется ответ для примера. В случае операции вычитания ответ должен быть положительным.
При делении ответ должен быть целым числом.

### Подсчет очков
В зависимости от операции начисляются очки:
* 1 очно за сложение;
* 2 очка за вычитание;
* 3 очка за умножение;
* 4 очка за деление.

Операнды при начислении очков не имеют значения, это означает, что 2х2 по начислению очков равно 23х22. 

### Уровни сложности
На первом уровне "Легкий" присутствуют только операции сложения и вычитания. Среди операндов может быть только
одно двузначное число.

На втором уровне "Средний" присутствуют операции умножения и деления. Среди операндов может быть только
одно двузначное число.

На третьем уровне "Сложный" есть все операции. Среди операндов для операций сложения должны быть два
трехзначных числа. Для вычитания и деления должны быть трех- и двузначное числа. Для умножения два двузначных.
