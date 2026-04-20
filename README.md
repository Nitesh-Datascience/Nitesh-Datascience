<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Nitesh Kumar | Data Analyst Portfolio</title>
  <meta name="description" content="Nitesh Kumar - Data Analyst portfolio featuring projects, skills, internships, certifications, and contact details." />
  <meta name="theme-color" content="#0b1220" />

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

  <style>
    :root {
      --bg: #0b1220;
      --bg-2: #111a2e;
      --panel: rgba(255, 255, 255, 0.06);
      --panel-2: #ffffff;
      --text: #e5eefc;
      --text-dark: #10203a;
      --muted: #9db0d0;
      --primary: #4f8cff;
      --accent: #22c55e;
      --border: rgba(255,255,255,.12);
      --shadow: 0 18px 40px rgba(8, 15, 32, .25);
      --radius: 24px;
    }

    * { box-sizing: border-box; scroll-behavior: smooth; }

    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background:
        radial-gradient(circle at top right, rgba(79,140,255,.18), transparent 22%),
        radial-gradient(circle at bottom left, rgba(34,197,94,.10), transparent 18%),
        linear-gradient(180deg, #09101d 0%, #0f172a 100%);
      color: var(--text);
    }

    a { text-decoration: none; }

    .navbar-custom {
      background: rgba(9, 16, 29, .72);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(255,255,255,.08);
    }

    .navbar-brand {
      font-weight: 800;
      letter-spacing: .4px;
    }

    .nav-link {
      color: #d7e3fb !important;
      font-weight: 500;
    }

    .nav-link:hover { color: #ffffff !important; }

    .hero {
      padding: 140px 0 90px;
      position: relative;
      overflow: hidden;
    }

    .badge-soft {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 16px;
      border-radius: 999px;
      background: rgba(255,255,255,.08);
      border: 1px solid var(--border);
      color: #dfeaff;
      font-size: .92rem;
      margin-bottom: 22px;
    }

    .hero h1 {
      font-size: clamp(2.5rem, 6vw, 4.8rem);
      line-height: 1.03;
      font-weight: 800;
      margin-bottom: 14px;
    }

    .gradient-text {
      background: linear-gradient(90deg, #ffffff, #9cc0ff 45%, #68f0a2 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .hero p {
      color: var(--muted);
      font-size: 1.06rem;
      max-width: 700px;
    }

    .hero-card,
    .glass,
    .stat-card,
    .skill-card,
    .project-card,
    .timeline-card,
    .contact-card {
      border: 1px solid var(--border);
      background: var(--panel);
      backdrop-filter: blur(12px);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }

    .hero-card { padding: 24px; }
    .glass { padding: 28px; }

    .profile-box {
      width: 160px;
      height: 160px;
      margin: 0 auto 18px;
      border-radius: 28px;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, rgba(79,140,255,.25), rgba(34,197,94,.16));
      border: 1px solid rgba(255,255,255,.15);
      font-size: 3rem;
      color: #fff;
      font-weight: 800;
    }

    .hero-meta {
      display: grid;
      gap: 10px;
      margin-top: 18px;
      color: #e7efff;
    }

    .hero-meta div {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: 14px;
      background: rgba(255,255,255,.04);
    }

    .btn-main {
      padding: 13px 24px;
      border-radius: 14px;
      font-weight: 700;
      border: 0;
    }

    .btn-primary-pro {
      background: linear-gradient(90deg, #4f8cff, #2d6df7);
      color: white;
    }

    .btn-outline-pro {
      background: transparent;
      color: white;
      border: 1px solid rgba(255,255,255,.16);
    }

    .section { padding: 84px 0; }

    .section-heading {
      text-align: center;
      margin-bottom: 44px;
    }

    .section-heading h2 {
      font-size: clamp(1.9rem, 4vw, 3rem);
      font-weight: 800;
      margin-bottom: 10px;
    }

    .section-heading p {
      color: var(--muted);
      max-width: 760px;
      margin: 0 auto;
    }

    .stats-grid {
      margin-top: 34px;
    }

    .stat-card {
      padding: 24px;
      height: 100%;
      text-align: center;
    }

    .stat-number {
      font-size: 2rem;
      font-weight: 800;
      color: white;
    }

    .about-panel {
      background: #ffffff;
      color: var(--text-dark);
      border-radius: var(--radius);
      padding: 34px;
      box-shadow: 0 16px 40px rgba(0,0,0,.14);
      height: 100%;
    }

    .about-panel p,
    .about-panel li { color: #53627d; }

    .mini-card {
      background: #f4f7fd;
      border-radius: 18px;
      padding: 20px;
      height: 100%;
    }

    .mini-card i {
      font-size: 1.4rem;
      color: var(--primary);
    }

    .skill-card,
    .project-card,
    .timeline-card,
    .contact-card {
      padding: 24px;
      height: 100%;
    }

    .skill-chip {
      display: inline-block;
      padding: 10px 14px;
      margin: 6px;
      border-radius: 999px;
      background: rgba(255,255,255,.08);
      border: 1px solid rgba(255,255,255,.09);
      color: #edf4ff;
      font-size: .95rem;
      font-weight: 500;
    }

    .icon-box {
      width: 56px;
      height: 56px;
      border-radius: 18px;
      display: grid;
      place-items: center;
      font-size: 1.4rem;
      color: white;
      background: linear-gradient(135deg, rgba(79,140,255,.95), rgba(34,197,94,.7));
      margin-bottom: 18px;
    }

    .project-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
    }

    .tag {
      display: inline-block;
      padding: 8px 12px;
      border-radius: 999px;
      font-size: .85rem;
      font-weight: 700;
      background: rgba(255,255,255,.08);
      color: #dce8ff;
      border: 1px solid rgba(255,255,255,.08);
    }

    .project-card ul {
      padding-left: 18px;
      color: var(--muted);
      margin-bottom: 0;
    }

    .timeline-item {
      border-left: 2px solid rgba(255,255,255,.14);
      padding-left: 18px;
      margin-bottom: 24px;
      position: relative;
    }

    .timeline-item::before {
      content: "";
      position: absolute;
      left: -7px;
      top: 5px;
      width: 12px;
      height: 12px;
      border-radius: 999px;
      background: #68f0a2;
    }

    .timeline-item p,
    .project-card p,
    .skill-card p,
    .contact-card p {
      color: var(--muted);
    }

    .contact-list a,
    .contact-list span {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 14px;
      border-radius: 14px;
      background: rgba(255,255,255,.05);
      color: #edf4ff;
      margin-bottom: 12px;
    }

    .contact-list a:hover {
      background: rgba(255,255,255,.09);
    }

    .footer {
      padding: 26px 0 40px;
      color: #b6c7e4;
      text-align: center;
    }

    .small-muted { color: var(--muted); }

    @media (max-width: 991px) {
      .hero {
        padding-top: 120px;
      }
    }
  </style>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container">
      <a class="navbar-brand" href="#home">Nitesh Kumar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navMenu">
        <ul class="navbar-nav ms-auto gap-lg-2">
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
        <div class="col-lg-7">
          <div class="badge-soft"><i class="bi bi-stars"></i> Data Analyst Portfolio • GitHub Ready • Fresher Friendly</div>
          <h1><span class="gradient-text">Nitesh Kumar</span></h1>
          <h3 class="fw-semibold mb-3">Data Analyst | Python | SQL | Excel | Power BI</h3>
          <p class="mb-4">
            Motivated BCA graduate with practical experience in data analytics, dashboard design, machine learning, and business reporting. I build projects that turn raw data into clear insights and useful decisions.
          </p>
          <div class="d-flex flex-wrap gap-3">
            <a href="#projects" class="btn btn-main btn-primary-pro">Explore Projects</a>
            <a href="#contact" class="btn btn-main btn-outline-pro">Hire Me</a>
          </div>

          <div class="row g-3 stats-grid">
            <div class="col-md-4">
              <div class="stat-card">
                <div class="stat-number" data-target="6">0</div>
                <div class="small-muted">Projects Built</div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="stat-card">
                <div class="stat-number" data-target="3">0</div>
                <div class="small-muted">Internships / Training</div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="stat-card">
                <div class="stat-number" data-target="10">0</div>
                <div class="small-muted">Core Tools</div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="hero-card text-center">
            <div class="profile-box">NK</div>
            <h4 class="mb-1">Nitesh Kumar</h4>
            <p class="small-muted mb-3">BCA Graduate • Data Analytics Learner • Open to Opportunities</p>
            <div class="hero-meta text-start">
              <div><i class="bi bi-envelope-fill"></i> ns0762005@gmail.com</div>
              <div><i class="bi bi-telephone-fill"></i> +91 9650410697</div>
              <div><i class="bi bi-geo-alt-fill"></i> Delhi, India</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="container">
      <div class="section-heading">
        <h2>About Me</h2>
        <p>A professional GitHub portfolio should show not only your skills, but also your value, project thinking, and career direction.</p>
      </div>

      <div class="row g-4 align-items-stretch">
        <div class="col-lg-7">
          <div class="about-panel">
            <h3 class="fw-bold mb-3">Professional Summary</h3>
            <p>
              I am a BCA graduate with a strong interest in data analytics, reporting, business intelligence, and machine learning. I enjoy working with Excel, SQL, Python, and Power BI to clean data, analyze patterns, build dashboards, and solve practical business problems.
            </p>
            <p>
              My goal is to start my career in data analytics, MIS reporting, or business intelligence, where I can contribute through dashboards, insights, and data-driven decision-making.
            </p>
            <div class="row g-3 mt-2">
              <div class="col-md-6">
                <div class="mini-card">
                  <i class="bi bi-graph-up-arrow mb-2 d-inline-block"></i>
                  <h5 class="mt-2">What I Do</h5>
                  <p class="mb-0">Dashboard creation, Excel reporting, SQL analysis, data cleaning, and beginner-friendly machine learning projects.</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="mini-card">
                  <i class="bi bi-lightning-charge-fill mb-2 d-inline-block"></i>
                  <h5 class="mt-2">My Strengths</h5>
                  <p class="mb-0">Quick learner, consistent practice mindset, project-based learning, presentation skills, and clear communication.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="about-panel">
            <h3 class="fw-bold mb-3">Quick Highlights</h3>
            <ul class="mb-0">
              <li class="mb-3">BCA graduate with focus on analytics and IT roles</li>
              <li class="mb-3">Hands-on work in Python, SQL, Excel, Power BI, and data visualization</li>
              <li class="mb-3">Experience through internships, simulations, and self-built projects</li>
              <li class="mb-3">Interested in Data Analyst, MIS Executive, Reporting Analyst, and BI roles</li>
              <li>Comfortable presenting insights in a simple, clear, and business-friendly way</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="skills">
    <div class="container">
      <div class="section-heading">
        <h2>Technical Skills</h2>
        <p>These are the main tools and technologies I use in projects, assignments, and portfolio work.</p>
      </div>

      <div class="row g-4 mb-4">
        <div class="col-md-4">
          <div class="skill-card">
            <div class="icon-box"><i class="bi bi-file-earmark-bar-graph"></i></div>
            <h5>Analytics & BI</h5>
            <p>Excel, Power BI, dashboard design, KPI tracking, reporting, pivot tables, charts, and business insights.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="skill-card">
            <div class="icon-box"><i class="bi bi-database-fill"></i></div>
            <h5>Data Handling</h5>
            <p>SQL queries, joins, filtering, aggregation, database concepts, data cleaning, and structured analysis.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="skill-card">
            <div class="icon-box"><i class="bi bi-code-slash"></i></div>
            <h5>Programming</h5>
            <p>Python fundamentals, pandas, machine learning basics, visualization, and practical project workflows.</p>
          </div>
        </div>
      </div>

      <div class="text-center">
        <span class="skill-chip">Python</span>
        <span class="skill-chip">SQL</span>
        <span class="skill-chip">Excel</span>
        <span class="skill-chip">Power BI</span>
        <span class="skill-chip">Machine Learning</span>
        <span class="skill-chip">Data Visualization</span>
        <span class="skill-chip">Pandas</span>
        <span class="skill-chip">NumPy</span>
        <span class="skill-chip">Canva</span>
        <span class="skill-chip">GitHub</span>
      </div>
    </div>
  </section>

  <section class="section" id="projects">
    <div class="container">
      <div class="section-heading">
        <h2>Featured Projects</h2>
        <p>A strong GitHub portfolio should focus on projects with clear tools, outcomes, and business value.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="project-card">
            <div class="project-top">
              <h4 class="mb-0">Sales MIS Dashboard</h4>
              <span class="tag">Excel + Power BI</span>
            </div>
            <p>Built an interactive MIS dashboard to analyze sales, profit, regional performance, and KPI trends for business reporting.</p>
            <ul>
              <li>Created pivot-based reporting and KPI summary cards</li>
              <li>Designed dashboard layout with slicers and charts</li>
              <li>Converted raw sales data into management-ready insights</li>
            </ul>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="project-card">
            <div class="project-top">
              <h4 class="mb-0">IPL Match Winner Prediction</h4>
              <span class="tag">Python + ML</span>
            </div>
            <p>Developed a machine learning project to predict IPL outcomes using match-related features and historical cricket data.</p>
            <ul>
              <li>Performed data preprocessing and feature preparation</li>
              <li>Tested predictive models for match results</li>
              <li>Presented a portfolio-friendly sports analytics use case</li>
            </ul>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="project-card">
            <div class="project-top">
              <h4 class="mb-0">Telecom Churn Analysis</h4>
              <span class="tag">Analytics + BI</span>
            </div>
            <p>Worked on churn-related customer data to identify retention patterns and visualize important factors behind customer loss.</p>
            <ul>
              <li>Used analytics workflow for data cleaning and exploration</li>
              <li>Built visual reports and business-facing interpretations</li>
              <li>Focused on churn trends and customer behavior insights</li>
            </ul>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="project-card">
            <div class="project-top">
              <h4 class="mb-0">Smart Water Tank Monitoring</h4>
              <span class="tag">IoT Project</span>
            </div>
            <p>Created an academic IoT project concept for smart water level tracking and efficient monitoring using sensors and automation ideas.</p>
            <ul>
              <li>Applied problem-solving to a real-world monitoring use case</li>
              <li>Connected analytics thinking with IoT workflow</li>
              <li>Prepared documentation and presentation-level explanation</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="experience">
    <div class="container">
      <div class="section-heading">
        <h2>Experience & Learning Journey</h2>
        <p>Recruiter like to see clear learning progression, internships, certifications, and practical exposure.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-7">
          <div class="timeline-card">
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">QSpiders</h5>
              <p class="mb-1">Training / internship exposure in analytics and software-related learning.</p>
              <span class="small-muted">Data Analytics • Python • Career preparation</span>
            </div>
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">Zidio - Data Science & Analytics Internship</h5>
              <p class="mb-1">Worked on data science and analytics learning tasks with hands-on practice.</p>
              <span class="small-muted">Analytics workflow • project exposure</span>
            </div>
            <div class="timeline-item">
              <h5 class="fw-bold mb-1">ShapeMySkills - Data Science & ML Training</h5>
              <p class="mb-1">Completed training in Python, machine learning, and deep learning fundamentals.</p>
              <span class="small-muted">Python • ML • DL • practice projects</span>
            </div>
            <div class="timeline-item mb-0">
              <h5 class="fw-bold mb-1">Simulations & Certifications</h5>
              <p class="mb-1">Forage simulations, Excel learning, analytics practice, and continuous project building.</p>
              <span class="small-muted">Self-learning • upskilling • portfolio growth</span>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="timeline-card">
            <h4 class="mb-4">Why This Portfolio Works</h4>
            <ul class="mb-0" style="color: var(--muted); padding-left: 18px;">
              <li class="mb-3">Professional dark theme with modern layout</li>
              <li class="mb-3">Focused on recruiter-friendly sections</li>
              <li class="mb-3">Built as a single file for easy GitHub Pages hosting</li>
              <li class="mb-3">Responsive design for desktop and mobile</li>
              <li class="mb-3">Simple to edit with your GitHub, LinkedIn, and project links</li>
              <li>Good starting point for a pro fresher portfolio</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="contact">
    <div class="container">
      <div class="section-heading">
        <h2>Contact</h2>
        <p>Replace the placeholder links below with your real LinkedIn, GitHub, resume, and portfolio project URLs.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="contact-card">
            <h4 class="mb-4">Get In Touch</h4>
            <div class="contact-list">
              <a href="mailto:ns0762005@gmail.com"><i class="bi bi-envelope-fill"></i> ns0762005@gmail.com</a>
              <a href="tel:+919650410697"><i class="bi bi-telephone-fill"></i> +91 9650410697</a>
              <span><i class="bi bi-geo-alt-fill"></i> Delhi, India</span>
              <a href="https://www.linkedin.com/" target="_blank"><i class="bi bi-linkedin"></i> Add your LinkedIn URL</a>
              <a href="https://github.com/" target="_blank"><i class="bi bi-github"></i> Add your GitHub URL</a>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="contact-card">
            <h4 class="mb-4">Quick Message</h4>
            <form id="contactForm">
              <div class="mb-3">
                <input type="text" class="form-control form-control-lg" placeholder="Your Name" required>
              </div>
              <div class="mb-3">
                <input type="email" class="form-control form-control-lg" placeholder="Your Email" required>
              </div>
              <div class="mb-3">
                <textarea rows="5" class="form-control" placeholder="Write your message" required></textarea>
              </div>
              <button class="btn btn-main btn-primary-pro w-100" type="submit">Send Message</button>
            </form>
            <div id="alertBox" class="mt-3"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <p class="mb-1">© 2026 Nitesh Kumar • Data Analyst Portfolio</p>
      <small>Built with HTML, CSS, Bootstrap, and JavaScript • Ready for GitHub Pages</small>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    const counters = document.querySelectorAll('.stat-number');

    const animateCounter = (counter) => {
      const target = +counter.dataset.target;
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
    }, { threshold: 0.4 });

    counters.forEach(counter => observer.observe(counter));

    document.getElementById('contactForm').addEventListener('submit', function(e) {
      e.preventDefault();
      document.getElementById('alertBox').innerHTML = '<div class="alert alert-success mb-0">Thanks! This demo portfolio captured your message locally.</div>';
      this.reset();
    });
  </script>
</body>
</html>
