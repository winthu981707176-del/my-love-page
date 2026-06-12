<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Timeless Love</title>
    <style>
        body { font-family: 'Georgia', serif; background-color: #fff0f5; text-align: center; margin: 0; padding-bottom: 80px; color: #4a4a4a; }
        .header { background: linear-gradient(135deg, #ff758c, #ff7eb3); color: white; padding: 40px 20px 60px; border-radius: 0 0 40px 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .header h1 { margin: 0; font-size: 26px; }
        
        .profile-container { display: flex; justify-content: center; margin-top: -50px; position: relative; z-index: 10; }
        .profile-img { width: 120px; height: 120px; border-radius: 50%; border: 5px solid white; object-fit: cover; box-shadow: 0 8px 20px rgba(255,105,180,0.3); }
        
        .card { background: white; padding: 25px; margin: 20px auto; border-radius: 20px; width: 85%; box-shadow: 0 10px 25px rgba(255,105,180,0.15); border: 1px solid #ffe4e1; box-sizing: border-box; }
        .timer-days { font-size: 26px; color: #ff4d6d; font-weight: bold; margin: 10px 0; font-family: sans-serif; }
        .timer-sub { font-size: 14px; color: #888; }
        
        /* Quiz Styles */
        .quiz-container { text-align: left; }
        .quiz-q { font-size: 16px; font-weight: bold; color: #d63384; margin-bottom: 15px; line-height: 1.5; text-align: center; }
        .quiz-btn { display: block; width: 100%; margin: 10px 0; padding: 14px; border: none; border-radius: 25px; background: linear-gradient(to right, #ff4d6d, #ff758c); color: white; font-size: 15px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 10px rgba(255,77,109,0.15); }
        .quiz-btn:active { transform: scale(0.98); }
        .quiz-progress { font-size: 13px; color: #888; text-align: center; margin-bottom: 10px; font-weight: bold; }
        
        /* Bottom Navigation Bar */
        .navbar { position: fixed; bottom: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #ffb6c1; box-shadow: 0 -4px 10px rgba(0,0,0,0.05); z-index: 100; }
        .nav-item { font-size: 13px; color: #ff4d6d; cursor: pointer; font-weight: bold; display: flex; flex-direction: column; align-items: center; gap: 4px; width: 25%; }
        .nav-item.active-nav { color: #b7094c; transform: scale(1.05); }

        .tab-content { display: none; animation: fadeIn 0.4s ease-in-out; }
        .active-tab { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .memory-box { margin-bottom: 20px; text-align: left; }
        .memory-box p { font-weight: bold; color: #d63384; margin-bottom: 8px; }
        .memory-img { width: 100%; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); object-fit: cover; }
    </style>
</head>
<body>

<div class="header">
    <h1>Our Timeless Journey 🌹</h1>
</div>

<div class="profile-container">
    <img src="hony.jpg" class="profile-img" alt="My Love">
</div>

<div id="home-tab" class="tab-content active-tab">
    <div class="card">
        <h3 style="color: #d63384; margin-top: 0;">ကိုတို့ရဲ့ အချစ်သက်တမ်း</h3>
        <div class="timer-days" id="love-counter">တွက်ချက်နေသည်...</div>
        <div class="timer-sub" id="love-detail">စက္ကန့်အထိ အသေးစိတ်ပြသပေးနေသည်</div>
    </div>
    
    <div class="card">
        <h3 style="color: #ff758c; margin-top: 0; margin-bottom: 5px;">အချစ်ရေး အမေးအဖြေ (Quiz) 💖</h3>
        <div class="quiz-progress" id="quiz-status">မေးခွန်း ၁ / ၁၀</div>
        <div class="quiz-container">
            <p class="quiz-q" id="question-text">တွက်ချက်နေသည်...</p>
            <div id="options-container"></div>
        </div>
    </div>
</div>

<div id="bday-tab" class="tab-content">
    <div class="card">
        <h3 style="color: #ff4d6d; margin-top: 0;">Birthday Countdown 🎂</h3>
        <p>အသည်းလေးရဲ့ မွေးနေ့ (ဒီဇင်ဘာ ၂၇) အတွက် စောင့်ဆိုင်းခြင်း 💖</p>
        <div class="timer-days" id="bday-counter">တွက်ချက်နေသည်...</div>
        <p style="color: #888; font-size: 13px;">မွေးနေ့ရောက်ဖို့ စက္ကန့်အလိုက် ရေတွက်နေပါတယ်နော်</p>
    </div>
</div>

<div id="memories-tab" class="tab-content">
    <div class="card">
        <h3 style="color: #ff4d6d; margin-top: 0;">တို့နှစ်ယောက်ရဲ့ အမှတ်တရကမ္ဘာ 📸</h3>
        
        <div class="memory-box">
            <p>✨ ဒါကိုတို့ ပထမဆုံး အတူတူရိုက်ဖူးတဲ့ပုံ</p>
            <img src="sweet.png" class="memory-img" alt="First Memory">
        </div>
        
        <div class="memory-box" style="margin-top: 25px;">
            <p>📜 ကိုယ့်နှလုံးသားထဲက စကားစု</p>
            <div style="background: #fff5f7; padding: 15px; border-radius: 12px; line-height: 1.6; font-style: italic;">
                "ကိုယ့်ဘဝထဲကို ရောက်လာပေးလို့ ကျေးဇူးအများကြီးတင်ပါတယ်တယ်... 🥰<br>
                မင်းနဲ့ ဆုံတွေ့ခဲ့ရတဲ့ နေ့ရက်တိုင်းက ကိုယ့်အတွက်တော့ တကယ့်ကို အဖိုးတန်ဆုံးပါပဲ။<br>
                နောင်နှစ်ပေါင်းများစွာအထိ အတူတူအိုမင်းကြမယ်နော်... 🌹"
            </div>
        </div>
    </div>
</div>

<div id="music-tab" class="tab-content">
    <div class="card">
        <h3 style="color: #ff4d6d; margin-top: 0;">တို့နှစ်ယောက်လုံး ကြိုက်တဲ့သီချင်းလေး 🎶</h3>
        
        <div style="margin-top: 20px;">
            <audio controls style="width: 100%;">
                <source src="soung-btn" type="audio/mpeg">
                <source src="soung-btn.mp3" type="audio/mpeg">
            </audio>
        </div>
        <p style="font-weight: bold; color: #ff4d6d; margin-top: 15px;">သီချင်း - ဘေးစကား 🎵</p>
    </div>
</div>

<div class="navbar">
    <div class="nav-item active-nav" id="nav-home" onclick="switchTab('home')"><span>🏠</span>Home</div>
    <div class="nav-item" id="nav-bday" onclick="switchTab('bday')"><span>🎂</span>Birthday</div>
    <div class="nav-item" id="nav-memories" onclick="switchTab('memories')"><span>📸</span>Memories</div>
    <div class="nav-item" id="nav-music" onclick="switchTab('music')"><span>🎶</span>Music</div>
</div>

<script>
    function switchTab(tabName) {
        document.getElementById('home-tab').classList.remove('active-tab');
        document.getElementById('bday-tab').classList.remove('active-tab');
        document.getElementById('memories-tab').classList.remove('active-tab');
        document.getElementById('music-tab').classList.remove('active-tab');
        
        document.getElementById('nav-home').classList.remove('active-nav');
        document.getElementById('nav-bday').classList.remove('active-nav');
        document.getElementById('nav-memories').classList.remove('active-nav');
        document.getElementById('nav-music').classList.remove('active-nav');
        
        document.getElementById(tabName + '-tab').classList.add('active-tab');
        document.getElementById('nav-' + tabName).classList.add('active-nav');
    }

    // ချစ်သူသက်တမ်းစတင်ချိန် (၂၀၂၅ ခုနှစ်၊ ဒီဇင်ဘာ ၁၂ ရက် ညနေ ၅ နာရီ)
    function updateLoveCounter() {
        var startDate = new Date("2025-12-12T16:00:00");
        var now = new Date();
        var diff = now - startDate;
        
        var days = Math.floor(diff / (1000 * 60 * 60 * 24));
        var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((diff % (1000 * 60)) / 1000);
        
        var counterEl = document.getElementById("love-counter");
        var detailEl = document.getElementById("love-detail");
        
        if (counterEl) {
            counterEl.innerHTML = days + " ရက်";
        }
        if (detailEl) {
            detailEl.innerHTML = "အတူရှိခဲ့တာ " + hours + " နာရီ " + minutes + " မိနစ် " + seconds + " စက္ကန့် ရှိပြီနော် 🥰";
        }
    }

    // မွေးနေ့ရက်စွဲအမှန် Countdown (ဒီဇင်ဘာ ၂၇)
    function updateBdayCounter() {
        var now = new Date();
        var bday = new Date(now.getFullYear(), 11, 27); // Month 11 คือ December (0-indexed)
        if (now > bday) bday.setFullYear(now.getFullYear() + 1);
        
        var diff = bday - now;
        var days = Math.floor(diff / (1000 * 60 * 60 * 24));
        var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((diff % (1000 * 60)) / 1000);
        
        var bdayEl = document.getElementById("bday-counter");
        if(bdayEl) bdayEl.innerHTML = days + " ရက် " + hours + " နာရီ " + minutes + " မိနစ် " + seconds + " စက္ကန့်";
    }

    // Quiz မေးခွန်း ၁၀ ခုလုံး ပြန်လည်သန့်စင်ထားသည်
    var quizData = [
        { q: "ကိုတို့စတွေ့တုန်းက မင့်တပါတ်လေးခြုံထားလား၊ မထားဘူးလား?", a: ["ခြုံထားပါတယ်ဗျာ 🥰", "မခြုံထားပါဘူးနော် ❌"], correct: 0 },
        { q: "ကိုတို့ စတင်လက်တွဲခဲ့ကြတဲ့ လက ဘယ်လလဲ?", a: ["နိုဝင်ဘာလ", "ဒီဇင်ဘာလ 💖"], correct: 1 },
        { q: "ကိုယ့်အသည်းလေးရဲ့ မွေးနေ့က ဘယ်နေ့လဲ?", a: ["ဒီဇင်ဘာ ၂၇ ရက် 🎂", "နိုဝင်ဘာ ၂၇ ရက်"], correct: 0 },
        { q: "ကိုတို့နှစ်ယောက် အဓိက သုံးပြီးစကားပြောဖြစ်တဲ့ App က ဘာလဲ?", a: ["Message 💬", "Viber"], correct: 0 },
        { q: "ကိုယ့်အသည်းလေး စိတ်ကောက်ရင် ကိုက ဘာလုပ်ပေးရမလဲ?", a: ["ချော့ရမယ် အလိုလိုက်ရမယ် 🥰", "ပစ်ထားရမယ်"], correct: 0 },
        { q: "ကိုတို့ ပထမဆုံး ဖုန်းပြောဖြစ်တာဘယ်တုန်းကလဲသိလား?", a: ["ကိုတို့ချစ်သူဖြစ်ပြီးနောက်နေ့", "မင့်ဘုရားဝတ်ပြုတုန်းက ⛪"], correct: 1 },
        { q: "မောင်က အသည်းလေးကို ဘယ်လိုခေါ်တာ ပိုကြိုက်လဲ?", a: ["အသည်းလေး / မင့် 💖", "ဟေ့လူ"], correct: 0 },
        { q: "ကိုတို့ စကားများရင် ဘယ်သူက အရင် လျှော့ပေးလေ့ရှိလဲ?", a: ["မောင် ကပဲ အမြဲလျှော့ပေးတယ် 🥰", "ဘယ်သူမှမလျှော့ဘူး"], correct: 0 },
        { q: "အသည်းလေး အကြိုက်ဆုံး မုန့်က ဘာလဲ?", a: ["မုန့်ပဲခြွေ 🍦", "အစပ်"], correct: 0 },
        { q: "ကိုယ့်အသည်းလေးကို မောင် ဘယ်လောက်အထိ ချစ်လဲ?", a: ["ကမ္ဘာပေါ်က အားလုံးထက် ပိုချစ်တယ် 🌍💞", "နည်းနည်းပဲ"], correct: 0 }
    ];

    var currentQuestionIndex = 0;

    function loadQuestion() {
        var statusEl = document.getElementById('quiz-status');
        var textEl = document.getElementById('question-text');
        var containerEl = document.getElementById('options-container');
        
        if(!statusEl || !textEl || !containerEl) return;

        if (currentQuestionIndex >= quizData.length) {
            statusEl.innerHTML = "Quiz အောင်မြင်သွားပါပြီ! 🎉";
            textEl.innerHTML = "မေးခွန်း ၁၀ ခုလုံး မှန်အောင် ဖြေနိုင်ခဲ့တယ်! တကယ်ချစ်တတ်တဲ့ အသည်းလေးပဲနော် 😘💖✨";
            containerEl.innerHTML = "";
            return;
        }
        
        statusEl.innerHTML = "မေးခွန်း " + (currentQuestionIndex + 1) + " / " + quizData.length;
        var currentQuiz = quizData[currentQuestionIndex];
        textEl.innerHTML = currentQuiz.q;
        
        var optionsHtml = "";
        for (var i = 0; i < currentQuiz.a.length; i++) {
            optionsHtml += '<button class="quiz-btn" onclick="selectOption(' + i + ')">' + currentQuiz.a[i] + '</button>';
        }
        containerEl.innerHTML = optionsHtml;
    }

    function selectOption(selectedIndex) {
        var currentQuiz = quizData[currentQuestionIndex];
        if (selectedIndex === currentQuiz.correct) {
            alert("မှန်တယ်! ကိုယ့်အသည်းလေးက တကယ်တော်တယ် 😘");
            currentQuestionIndex++;
            loadQuestion();
        } else {
            alert("မှားသွားပြီကွာ... စိတ်မဆိုးနဲ့နော် နောက်တစ်ခေါက် ပြန်စဉ်းစားပြီး ဖြေကြည့်ပါဦး 😅💕");
        }
    }

    setInterval(function() { updateLoveCounter(); updateBdayCounter(); }, 1000);
    
    window.onload = function() {
        updateLoveCounter();
        updateBdayCounter();
        loadQuestion();
    };
</script>
</body>
</html>
