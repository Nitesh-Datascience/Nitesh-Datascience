<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Nitesh Kumar | Data Analytics Portfolio</title>
  <meta name="description" content="Portfolio website of Nitesh Kumar - BCA fresher, Data Analytics, Python, SQL, Excel, Power BI, Machine Learning." />

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

  <style>
    :root {
      --primary: #0d6efd;
      --dark: #0f172a;
      --dark-2: #1e293b;
      --light: #f8fafc;
      --muted: #64748b;
      --card: #ffffff;
      --accent: #f59e0b;
      --shadow: 0 18px 45px rgba(15, 23, 42, 0.10);
      --radius: 22px;
    }

    * {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Poppins', sans-serif;
      background: #f1f5f9;
      color: var(--dark);
    }

    .navbar-custom {
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(8px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }

    .navbar-brand {
      font-weight: 800;
      letter-spacing: 0.5px;
    }

    .hero {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.94), rgba(13, 110, 253, 0.88));
      color: white;
      padding: 150px 0 90px;
      position: relative;
      overflow: hidden;
    }

    .hero::before,
    .hero::after {
      content: "";
      position: absolute;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      z-index: 0;
    }

    .hero::before {
      width: 320px;
      height: 320px;
      top: -120px;
      right: -60px;
    }

    .hero::after {
      width: 220px;
      height: 220px;
      bottom: -90px;
      left: -50px;
    }

    .hero-content,
    .hero-card {
      position: relative;
      z-index: 1;
    }

    .hero-badge {
      display: inline-block;
      padding: 10px 18px;
      border-radius: 999px;
      background: rgba(255,255,255,0.14);
      border: 1px solid rgba(255,255,255,0.18);
      margin-bottom: 20px;
      font-size: 0.9rem;
    }

    .hero h1 {
      font-size: clamp(2.2rem, 5vw, 4rem);
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 15px;
    }

    .hero .lead {
      color: rgba(255,255,255,0.88);
      max-width: 680px;
    }

    .glass-card {
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: var(--radius);
      padding: 28px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.12);
    }

    .section {
      padding: 88px 0;
    }

    .section-title {
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 10px;
    }

    .section-subtitle {
      color: var(--muted);
      max-width: 650px;
      margin: 0 auto 45px;
    }

    .card-pro {
      background: var(--card);
      border: 0;
      border-radius: var(--radius);
      padding: 28px;
      box-shadow: var(--shadow);
      height: 100%;
      transition: 0.3s ease;
    }

    .card-pro:hover {
      transform: translateY(-6px);
    }

    .icon-wrap {
      width: 58px;
      height: 58px;
      border-radius: 16px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: rgba(13, 110, 253, 0.10);
      color: var(--primary);
      font-size: 1.35rem;
      margin-bottom: 16px;
    }

    .about-box,
    .contact-box,
    .resume-box {
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 34px;
      height: 100%;
    }

    .profile-pic {
      width: 100%;
      max-width: 360px;
      border-radius: 28px;
      object-fit: cover;
      border: 6px solid #fff;
      box-shadow: var(--shadow);
    }

    .skill-chip {
      display: inline-block;
      padding: 10px 16px;
      margin: 6px;
      border-radius: 999px;
      background: #e2e8f0;
      color: var(--dark-2);
      font-weight: 500;
      font-size: 0.95rem;
    }

    .timeline-item {
      position: relative;
      padding-left: 22px;
      margin-bottom: 24px;
      border-left: 2px solid #cbd5e1;
    }

    .timeline-item::before {
      content: "";
      position: absolute;
      left: -8px;
      top: 6px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--primary);
    }

    .project-card .badge,
    .timeline-item .badge {
      border-radius: 999px;
      padding: 8px 12px;
      font-weight: 500;
    }

    .counter-box {
      background: linear-gradient(135deg, #0f172a, #1d4ed8);
      color: #fff;
      border-radius: 24px;
      padding: 26px;
      box-shadow: var(--shadow);
      text-align: center;
      height: 100%;
    }

    .counter-number {
      font-size: 2rem;
      font-weight: 800;
      display: block;
    }

    .footer {
      background: #020617;
      color: #cbd5e1;
      padding: 24px 0;
    }

    .contact-link {
      text-decoration: none;
      color: var(--dark);
    }

    .contact-link:hover {
      color: var(--primary);
    }

    .btn-custom {
      border-radius: 14px;
      padding: 12px 22px;
      font-weight: 600;
    }

    @media (max-width: 991px) {
      .hero {
        padding: 130px 0 70px;
      }

      .profile-pic {
        max-width: 280px;
      }
    }
  </style>
</head>
<body>

  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container">
      <a class="navbar-brand" href="#home">Nitesh Portfolio</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-2">
          <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
          <li class="nav-item"><a class="nav-link" href="#skills">Skills</a></li>
          <li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
          <li class="nav-item"><a class="nav-link" href="#experience">Experience</a></li>
          <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <section class="hero" id="home">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-lg-7 hero-content">
          <div class="hero-badge"><i class="bi bi-stars me-2"></i>Data Analytics • Python • SQL • Power BI</div>
          <h1>Nitesh Kumar</h1>
          <h4 class="fw-semibold mb-3">BCA Fresher | Data Analyst | AI & ML Learner</h4>
          <p class="lead mb-4">
            Motivated and detail-oriented BCA student with a strong foundation in data science, analytics, machine learning, Python, SQL, Excel, Power BI, and data visualization.
          </p>
          <div class="d-flex flex-wrap gap-3">
            <a href="#projects" class="btn btn-light btn-custom">View Projects</a>
            <a href="#contact" class="btn btn-outline-light btn-custom">Contact Me</a>
          </div>
        </div>
        <div class="col-lg-5 hero-card text-center">
          <div class="glass-card">
           <img src="{{ url_for('static', filename='nitesh kumar.jpeg') }}" 
     alt="Nitesh Kumar" 
     class="profile-pic">
            <div class="row g-3 text-start">
              <div class="col-12">
                <div><i class="bi bi-envelope-fill me-2"></i>ns0762005@gmail.com</div>
              </div>
              <div class="col-12">
                <div><i class="bi bi-telephone-fill me-2"></i>+91 9650410697</div>
              </div>
              <div class="col-12">
                <div><i class="bi bi-geo-alt-fill me-2"></i>Delhi, India</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title">About Me</h2>
        <p class="section-subtitle">A fresher portfolio website built with HTML, CSS, Bootstrap, and JavaScript to showcase profile, projects, skills, and experience.</p>
      </div>

      <div class="row g-4 align-items-stretch">
        <div class="col-lg-7">
          <div class="about-box">
            <h3 class="fw-bold mb-3">Professional Summary</h3>
            <p class="text-secondary mb-4">
              I am a motivated BCA student with practical exposure to analytics, machine learning, and dashboard-based projects. I have completed internship and training experiences in data science and analytics, and I enjoy solving problems using data-driven thinking.
            </p>
            <div class="row g-3">
              <div class="col-md-6">
                <div class="card-pro h-100 p-4">
                  <div class="icon-wrap"><i class="bi bi-lightbulb"></i></div>
                  <h5>Soft Skills</h5>
                  <p class="mb-0 text-secondary">Problem-solving, critical thinking, teamwork, time management, adaptability, and resilience.</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="card-pro h-100 p-4">
                  <div class="icon-wrap"><i class="bi bi-translate"></i></div>
                  <h5>Languages & Interests</h5>
                  <p class="mb-0 text-secondary">English, Hindi, cricket, music, reading, traveling, and Canva design.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="resume-box">
            <h3 class="fw-bold mb-3">Quick Highlights</h3>
            <div class="timeline-item">
              <h6 class="mb-1 fw-bold">Education</h6>
              <p class="mb-0 text-secondary">Bachelor of Computer Application</p>
            </div>
            <div class="timeline-item">
              <h6 class="mb-1 fw-bold">Internships & Training</h6>
              <p class="mb-0 text-secondary">Data Science & Analytics internship exposure with ML and analytics tools.</p>
            </div>
            <div class="timeline-item mb-0">
              <h6 class="mb-1 fw-bold">Career Goal</h6>
              <p class="mb-0 text-secondary">To begin my career in analytics, data science, or IT roles and contribute to real-world projects.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white" id="skills">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title">Technical Skills</h2>
        <p class="section-subtitle">My current toolkit based on study, internship exposure, and practice projects.</p>
      </div>

      <div class="row g-4 mb-4">
        <div class="col-md-4">
          <div class="card-pro text-center">
            <div class="icon-wrap"><i class="bi bi-code-slash"></i></div>
            <h5>Programming</h5>
            <p class="text-secondary mb-0">Python, SQL, basic web development</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card-pro text-center">
            <div class="icon-wrap"><i class="bi bi-bar-chart-fill"></i></div>
            <h5>Analytics Tools</h5>
            <p class="text-secondary mb-0">Excel, Power BI, data visualization</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card-pro text-center">
            <div class="icon-wrap"><i class="bi bi-palette-fill"></i></div>
            <h5>Creative Tools</h5>
            <p class="text-secondary mb-0">Canva, presentation and design support</p>
          </div>
        </div>
      </div>

      <div class="text-center">
        <span class="skill-chip">Python</span>
        <span class="skill-chip">SQL</span>
        <span class="skill-chip">Excel</span>
        <span class="skill-chip">Power BI</span>
        <span class="skill-chip">Canva</span>
        <span class="skill-chip">Machine Learning</span>
        <span class="skill-chip">Deep Learning</span>
        <span class="skill-chip">Data Visualization</span>
        <span class="skill-chip">AI Basics</span>
        <span class="skill-chip">ChatGPT</span>
      </div>
    </div>
  </section>

  <section class="section" id="projects">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title">Projects</h2>
        <p class="section-subtitle">A few project ideas and practical work areas highlighted from my resume profile.</p>
      </div>

      <div class="row g-4">
        <div class="col-md-6 col-lg-4">
          <div class="card-pro project-card">
            <span class="badge bg-primary-subtle text-primary mb-3">ML Project</span>
            <h5>Nifty Prediction</h5>
            <p class="text-secondary">Built prediction models using LSTM, linear regression, SVM, decision tree, and KNN to forecast stock index performance.</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-4">
          <div class="card-pro project-card">
            <span class="badge bg-success-subtle text-success mb-3">Analytics Project</span>
            <h5>Telecom Churn Modeling</h5>
            <p class="text-secondary">Worked on data preprocessing, machine learning and deep learning modeling, plus dashboard visualization using Power BI.</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-4">
          <div class="card-pro project-card">
            <span class="badge bg-warning-subtle text-warning mb-3">IoT Project</span>
            <h5>Smart Water Tank Monitoring</h5>
            <p class="text-secondary">Developed an IoT-based idea focused on improving water monitoring efficiency using sensors and smart tracking concepts.</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-6">
          <div class="card-pro project-card">
            <span class="badge bg-danger-subtle text-danger mb-3">Prediction Project</span>
            <h5>Cars Dataset Prediction</h5>
            <p class="text-secondary mb-0">Personal practice project focused on data prediction and pattern analysis using different models.</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-6">
          <div class="card-pro project-card">
            <span class="badge bg-info-subtle text-info mb-3">Portfolio Ready</span>
            <h5>More Coming Soon</h5>
            <p class="text-secondary mb-0">This section can be updated with GitHub links, live project demos, and certificates as you complete more real projects.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-white" id="experience">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title">Internships, Training & Certifications</h2>
        <p class="section-subtitle">My learning journey through internships, training programs, and simulations.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-7">
          <div class="about-box">
            <h4 class="fw-bold mb-4">Experience Timeline</h4>
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">SHAPEMYSKILLS PRIVATE LIMITED</h5>
              <span class="badge bg-primary-subtle text-primary mb-2">6 weeks</span>
              <p class="mb-0 text-secondary">Data Science & ML Intern, including Python, machine learning, and deep learning summer training.</p>
            </div>
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">Zidio Development</h5>
              <span class="badge bg-success-subtle text-success mb-2">1 month</span>
              <p class="mb-0 text-secondary">Data Science & Analytics internship experience with practical exposure to analytics work.</p>
            </div>
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">Qspider Development</h5>
              <span class="badge bg-warning-subtle text-warning mb-2">6 months</span>
              <p class="mb-0 text-secondary">Worked around data analytics and Python development learning.</p>
            </div>
            <div class="timeline-item mb-0">
              <h5 class="fw-bold mb-1">Job Simulations & Learning</h5>
              <p class="mb-0 text-secondary">J.P. Morgan Quantitative Research, Deloitte Australia Data Analytics, Tata GenAI Analytics, Forage Data Labeling, Microsoft Excel with AI, and Canva Essentials.</p>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="row g-4">
            <div class="col-12">
              <div class="counter-box">
                <span class="counter-number" data-target="4">0</span>
                <p class="mb-0">Highlighted Projects</p>
              </div>
            </div>
            <div class="col-12">
              <div class="counter-box">
                <span class="counter-number" data-target="2">0</span>
                <p class="mb-0">Key Internships</p>
              </div>
            </div>
            <div class="col-12">
              <div class="counter-box">
                <span class="counter-number" data-target="8">0</span>
                <p class="mb-0">Tools & Skills</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="contact">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title">Contact Me</h2>
        <p class="section-subtitle">Open to fresher roles, internships, project collaborations, and analytics opportunities.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="contact-box">
            <h4 class="fw-bold mb-4">Get In Touch</h4>
            <p class="text-secondary">You can use this section to share your email, phone, LinkedIn, GitHub, and resume download button later.</p>
            <div class="mb-3">
              <a href="mailto:ns0762005@gmail.com" class="contact-link"><i class="bi bi-envelope-fill me-2"></i>ns0762005@gmail.com</a>
            </div>
            <div class="mb-3">
              <a href="tel:+919650410697" class="contact-link"><i class="bi bi-telephone-fill me-2"></i>+91 9650410697</a>
            </div>
            <div class="mb-3">
              <span><i class="bi bi-geo-alt-fill me-2"></i>Delhi, India</span>
            </div>
            <div class="d-flex gap-3 mt-4 flex-wrap">
              <a href="#" class="btn btn-primary btn-custom"><i class="bi bi-linkedin me-2"></i>LinkedIn</a>
              <a href="#" class="btn btn-dark btn-custom"><i class="bi bi-github me-2"></i>GitHub</a>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="contact-box">
            <h4 class="fw-bold mb-4">Quick Message</h4>
            <form id="contactForm">
              <div class="mb-3">
                <input type="text" id="name" class="form-control form-control-lg" placeholder="Your Name" required>
              </div>
              <div class="mb-3">
                <input type="email" id="email" class="form-control form-control-lg" placeholder="Your Email" required>
              </div>
              <div class="mb-3">
                <textarea id="message" rows="5" class="form-control" placeholder="Write your message" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-custom w-100">Send Message</button>
            </form>
            <div id="formAlert" class="mt-3"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer text-center">
    <div class="container">
      <p class="mb-1">© 2026 Nitesh Kumar Portfolio</p>
      <small>Built with HTML, CSS, Bootstrap, and JavaScript</small>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    const counters = document.querySelectorAll('.counter-number');

    const animateCounter = (counter) => {
      const target = +counter.getAttribute('data-target');
      let current = 0;
      const increment = Math.max(1, Math.ceil(target / 40));

      const update = () => {
        current += increment;
        if (current >= target) {
          counter.textContent = target;
        } else {
          counter.textContent = current;
          requestAnimationFrame(update);
        }
      };

      update();
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));

    document.getElementById('contactForm').addEventListener('submit', function(e) {
      e.preventDefault();
      document.getElementById('formAlert').innerHTML = `
        <div class="alert alert-success mb-0">Thank you! Your message has been captured in this demo portfolio.</div>
      `;
      this.reset();
    });
  </script>
</body>
</html>
