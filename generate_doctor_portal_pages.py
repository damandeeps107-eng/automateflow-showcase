import os

OUTPUT_DIR = "/Users/user/.gemini/antigravity/scratch/automateflow-showcase"

# Specialty-specific curated 3-slide cinematic hero images
DENTAL_SLIDES = [
    "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1598256989800-fe5f95da9787?auto=format&fit=crop&w=1600&q=80",
]

DERMA_SLIDES = [
    "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=1600&q=80",
]

DOCTORS = [
    {
        "slug": "dr-abhishek-jain-dental",
        "clinic_name": "Jain Advance Dental Care & Implant Center",
        "logo_title": "Jain Advance Dental",
        "logo_sub": "IMPLANT CENTER",
        "doctor_name": "Dr. Abhishek Jain",
        "degrees": "BDS, MDS — Implantology & Oral Surgery",
        "city": "Gurgaon",
        "phone": "918755207815",
        "phone_display": "+91 87552 07815",
        "rating": "4.8★",
        "reviews": "220+ Reviews",
        "category": "dental",
        "slides": DENTAL_SLIDES,
        "hero": [
            ("4.8★ Verified • 220+ Reviews • Gurgaon", "Precision Dental <span class='text-praanOrange'>Implants</span> & Painless Care.", "Led by Dr. Abhishek Jain (MDS), Gurgaon's trusted center for computer-guided dental implants, single-sitting root canals, and invisible aligners."),
            ("Digital 3D Smile Design", "Restore Your <span class='text-praanOrange'>Natural Smile</span> In One Visit.", "100% Class-B autoclaved sterilization, painless computerized anesthesia, and natural zirconia crowns crafted to last."),
            ("Direct VIP Appointment Portal", "Skip The <span class='text-praanOrange'>Waiting Room</span> Queue.", "Book your preferred consultation slot directly with Dr. Abhishek Jain's desk and receive an instant WhatsApp pass.")
        ],
        "marquee": ["JAIN ADVANCE DENTAL CARE", "DR. ABHISHEK JAIN (MDS)", "GUIDED DENTAL IMPLANTS", "PAINLESS SINGLE-SITTING RCT", "4.8★ (220+ REVIEWS) • GURGAON"],
        "programs": [
            ("Implants", "Guided Dental Implants", "Computer-assisted titanium & Swiss implants with lifelong structural stability."),
            ("Endodontics", "Painless Single-Sitting RCT", "Microscopic, painless root canal treatment completed comfortably in one sitting."),
            ("Aesthetics", "Invisible Aligners & Veneers", "3D digital smile designing with clear aligners and ultra-thin porcelain veneers."),
            ("Oral Surgery", "Wisdom Tooth & Full Rehab", "Minimally invasive surgical extractions and full-mouth implant rehabilitation.")
        ],
        "focus_options": ["Dental Implants", "Painless RCT", "Clear Aligners", "Smile Design"],
        "modes": ["Clinic Visit (Gurgaon)", "Video Consult", "Priority Implant Slot"],
        "steps": [
            ("3D Digital Scan & Checkup", "Detailed intraoral evaluation, digital X-ray & root-cause review with Dr. Abhishek Jain."),
            ("Transparent Treatment Plan", "Clear timeline, painless protocol, and zero hidden charges before starting any procedure."),
            ("Sterilized Precision Care", "World-class implant & restorative execution with automated WhatsApp follow-up care.")
        ]
    },
    {
        "slug": "dr-bansal-dental",
        "clinic_name": "Dr Bansal's Dental & Implant Clinic",
        "logo_title": "Dr. Bansal's Dental",
        "logo_sub": "IMPLANT CLINIC",
        "doctor_name": "Dr. Bansal",
        "degrees": "BDS, MDS — Implantology & Oral Surgery",
        "city": "Gurgaon",
        "phone": "919599661324",
        "phone_display": "+91 95996 61324",
        "rating": "4.8★",
        "reviews": "579+ Reviews",
        "category": "dental",
        "slides": DENTAL_SLIDES,
        "hero": [
            ("4.8★ Verified • 579+ Reviews • Gurgaon", "Trusted Dental <span class='text-praanOrange'>Implants</span> & Family Care.", "Led by Dr. Bansal, rated 4.8★ across 579+ patients in Gurgaon for painless implants, root canals, and cosmetic dentistry."),
            ("Microscopic Endodontics", "Painless <span class='text-praanOrange'>Single-Sitting</span> Root Canals.", "Advanced rotary endodontics and digital imaging ensuring gentle, zero-anxiety dental care for every age."),
            ("Direct VIP Appointment Portal", "Book Direct With <span class='text-praanOrange'>Dr. Bansal</span>.", "Choose your exact morning or evening consultation slot and get instant WhatsApp confirmation.")
        ],
        "marquee": ["DR BANSAL'S DENTAL CLINIC", "579+ VERIFIED REVIEWS (4.8★)", "GUIDED DENTAL IMPLANTS", "PAINLESS ROOT CANAL", "GURGAON'S TRUSTED PRACTICE"],
        "programs": [
            ("Implants", "Permanent Dental Implants", "Immediate-load and conventional implants with high long-term success rates."),
            ("Pain Relief", "Painless Root Canal", "Gentle single-visit RCT with computerized local anesthesia."),
            ("Cosmetic", "Smile Makeover & Crowns", "Natural-shade zirconia crowns, veneers, and laser teeth whitening."),
            ("Orthodontics", "Braces & Clear Aligners", "Customized teeth alignment solutions for teens and working professionals.")
        ],
        "focus_options": ["Dental Implants", "Painless RCT", "Zirconia Crowns", "Aligners / Braces"],
        "modes": ["Clinic Visit (Gurgaon)", "Video Consult", "Emergency Pain Slot"],
        "steps": [
            ("Comprehensive Oral Exam", "Complete dental assessment & digital X-ray evaluation directly with Dr. Bansal."),
            ("Personalized Care Roadmap", "Step-by-step clinical plan tailored to your comfort, timeline, and budget."),
            ("Long-Term Smile Protection", "Precision treatment with Class-B sterilization and scheduled follow-ups.")
        ]
    },
    {
        "slug": "dr-lokesh-dental",
        "clinic_name": "Prime Dental Care & Implant Centre",
        "logo_title": "Prime Dental Care",
        "logo_sub": "DR. LOKESH • IMPLANTS",
        "doctor_name": "Dr. Lokesh",
        "degrees": "BDS, MDS — Oral Implantologist",
        "city": "Gurgaon",
        "phone": "919034194858",
        "phone_display": "+91 90341 94858",
        "rating": "4.8★",
        "reviews": "419+ Reviews",
        "category": "dental",
        "slides": DENTAL_SLIDES,
        "hero": [
            ("4.8★ Verified • 419+ Reviews • Gurgaon", "Advanced <span class='text-praanOrange'>Implantology</span> & Smile Design.", "Prime Dental Care led by Dr. Lokesh — Gurgaon's 4.8★ rated center for full-mouth implants, laser gum care, and cosmetic dentistry."),
            ("Laser & Digital Dentistry", "Precision Care With <span class='text-praanOrange'>Zero Discomfort</span>.", "Modern rotary instruments, digital smile previews, and strict European sterilization standards."),
            ("Direct VIP Appointment Portal", "Reserve Your <span class='text-praanOrange'>Priority Slot</span> Online.", "Skip phone queues and confirm your appointment straight with Dr. Lokesh's clinic desk on WhatsApp.")
        ],
        "marquee": ["PRIME DENTAL CARE", "DR. LOKESH • GURGAON", "419+ VERIFIED REVIEWS (4.8★)", "IMMEDIATE DENTAL IMPLANTS", "LASER & COSMETIC DENTISTRY"],
        "programs": [
            ("Implantology", "Immediate Load Implants", "Fixed teeth solutions & single-tooth implants with 3D precision placement."),
            ("Laser Care", "Laser Gum & Painless RCT", "Bloodless laser gum contouring and single-sitting microscopic root canals."),
            ("Aesthetics", "Digital Smile Designing", "Porcelain veneers, metal-free zirconia crowns, and instant whitening."),
            ("Aligners", "Invisible Teeth Aligners", "Discreet, removable clear aligners mapped via 3D intraoral scanning.")
        ],
        "focus_options": ["Immediate Implants", "Laser Dentistry", "Smile Designing", "Clear Aligners"],
        "modes": ["Clinic Visit (Gurgaon)", "Video Consult", "Implant Evaluation"],
        "steps": [
            ("3D Evaluation & Consultation", "Root-cause diagnosis & digital scan led directly by Dr. Lokesh."),
            ("Custom Treatment Blueprint", "Transparent clinical options with clear session timelines and comfort guarantee."),
            ("Precision Execution & Follow-Up", "Sterilized clinical care with seamless WhatsApp post-care guidance.")
        ]
    },
    {
        "slug": "dr-rashmi-derma",
        "clinic_name": "Dr Rashmi Agrawal Dermatology & Laser Clinic",
        "logo_title": "Dr. Rashmi Agrawal",
        "logo_sub": "DERMATOLOGY & LASER",
        "doctor_name": "Dr. Rashmi Agrawal",
        "degrees": "MBBS, MD — Dermatology & Cosmetology",
        "city": "Noida",
        "phone": "919971731355",
        "phone_display": "+91 99717 31355",
        "rating": "4.8★",
        "reviews": "212+ Reviews",
        "category": "derma",
        "slides": DERMA_SLIDES,
        "hero": [
            ("4.8★ Verified • 212+ Reviews • Noida", "Clinical <span class='text-praanOrange'>Dermatology</span> & US-FDA Lasers.", "Led by Dr. Rashmi Agrawal (MD Dermatology), Noida's trusted clinic for evidence-based skin, hair, and aesthetic laser treatments."),
            ("Skin & Hair Restoration", "Restore Natural <span class='text-praanOrange'>Radiance</span> Safely.", "Doctor-performed chemical peels, acne scar resurfacing, anti-aging protocols, and medical hair regrowth."),
            ("Direct VIP Appointment Portal", "Consult <span class='text-praanOrange'>Dr. Rashmi</span> Without Waiting.", "Pick your preferred time slot below and receive an instant WhatsApp booking slip from our Noida desk.")
        ],
        "marquee": ["DR. RASHMI AGRAWAL (MD DERMA)", "212+ VERIFIED REVIEWS (4.8★)", "US-FDA LASER HAIR REDUCTION", "ACNE SCAR & PIGMENTATION", "NOIDA'S PREMIER SKIN CLINIC"],
        "programs": [
            ("Laser Care", "US-FDA Laser Hair Removal", "Painless, safe diode & triple-wavelength laser sessions for Indian skin tones."),
            ("Skin Clarity", "Acne, Scars & Melasma", "Medical-grade peels, MNRF, and customized protocols for clear, even-toned skin."),
            ("Anti-Aging", "Medi-Facials & Rejuvenation", "HydraFacial MD, Botox, dermal fillers, and collagen-boosting skin boosters."),
            ("Hair Regrowth", "PRP & GFC Hair Therapy", "Dermatologist-led hair fall control and follicular density restoration.")
        ],
        "focus_options": ["Acne & Pigmentation", "Laser Hair Removal", "Hair Fall / PRP", "Medi-Facial / Glow"],
        "modes": ["Clinic Visit (Noida)", "Video Skin Consult", "Laser Session"],
        "steps": [
            ("In-Depth Skin & Scalp Analysis", "Detailed dermatological evaluation directly with Dr. Rashmi Agrawal (MD)."),
            ("Evidence-Based Skin Roadmap", "Personalized blend of clinical actives, US-FDA lasers, and gentle home care."),
            ("Visible, Safe Transformation", "Tracked session-by-session improvements with direct WhatsApp follow-up.")
        ]
    },
    {
        "slug": "dr-sukriti-derm",
        "clinic_name": "Cure Derm Skin Clinic",
        "logo_title": "Cure Derm Clinic",
        "logo_sub": "DR. SUKRITI SHARMA (MD)",
        "doctor_name": "Dr. Sukriti Sharma",
        "degrees": "MBBS, MD — Consultant Dermatologist",
        "city": "Noida",
        "phone": "919899496133",
        "phone_display": "+91 98994 96133",
        "rating": "4.8★",
        "reviews": "240+ Reviews",
        "category": "derma",
        "slides": DERMA_SLIDES,
        "hero": [
            ("4.8★ Verified • 240+ Reviews • Noida", "Doctor-Led <span class='text-praanOrange'>Skin, Hair</span> & Laser Aesthetics.", "At Cure Derm Skin Clinic, Dr. Sukriti Sharma (MD) combines clinical dermatology with safe aesthetic lasers for lasting results."),
            ("Pigmentation & Acne Mastery", "Clear, Healthy <span class='text-praanOrange'>Skin</span> Backed By Science.", "Targeted medical solutions for stubborn melasma, active acne, scars, and hair thinning."),
            ("Direct VIP Appointment Portal", "Book Directly With <span class='text-praanOrange'>Cure Derm</span>.", "Select your consultation focus and preferred time slot for instant WhatsApp confirmation.")
        ],
        "marquee": ["CURE DERM SKIN CLINIC", "DR. SUKRITI SHARMA (MD)", "240+ VERIFIED REVIEWS (4.8★)", "CARBON LASER & HYDRAFACIAL", "NOIDA'S TRUSTED SKIN CARE"],
        "programs": [
            ("Clinical Skin", "Acne & Pigmentation Care", "Targeted dermatological treatments for melasma, dark spots, and acne scars."),
            ("Hair Solutions", "GFC & PRP Hair Restoration", "Science-backed scalp therapies to arrest hair fall and boost density."),
            ("Aesthetic Glow", "Carbon Laser & Medi-Facials", "Zero-downtime bridal glow, glass-skin facials, and collagen rejuvenation."),
            ("Lasers", "Permanent Laser Hair Reduction", "Comfortable, dermatologist-supervised laser sessions for smooth skin.")
        ],
        "focus_options": ["Acne & Pigmentation", "Hair Fall / GFC", "Medi-Facial / Glow", "Laser Reduction"],
        "modes": ["Clinic Visit (Noida)", "Video Consult", "Bridal / Skin Package"],
        "steps": [
            ("Clinical Skin Consultation", "Root-cause dermatological diagnosis directly with Dr. Sukriti Sharma."),
            ("Customized Protocol Design", "Safe, transparent treatment plan tailored specifically to your skin type."),
            ("Guided Progress & Support", "Measured results across sessions with direct WhatsApp care desk support.")
        ]
    }
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{clinic_name} | {doctor_name} — {city}</title>
  <meta name="description" content="{doctor_name} ({degrees}) — {clinic_name} in {city}. {rating} verified across {reviews}." />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            deepTeal: '#0E2421',
            praanOrange: '#F1631C',
            praanSoft: '#FFF3EC',
            ivory: '#FAF8F5',
            mist: '#F2F5F4',
            slateInk: '#475569'
          }},
          fontFamily: {{
            display: ['Manrope', 'sans-serif'],
            sans: ['Inter', 'sans-serif']
          }}
        }}
      }}
    }};
  </script>

  <style>
    :root {{ --ease: cubic-bezier(0.22, 1, 0.36, 1); }}
    html, body {{ margin: 0; padding: 0; background: #FAF8F5; color: #0E2421; font-family: 'Inter', sans-serif; overflow-x: hidden; -webkit-font-smoothing: antialiased; }}
    .typo-hero {{ font-family: 'Manrope', sans-serif; font-size: clamp(2.35rem, 5vw, 4.5rem); font-weight: 700; line-height: 1.06; letter-spacing: -0.03em; }}
    .typo-h2 {{ font-family: 'Manrope', sans-serif; font-size: clamp(1.85rem, 3.4vw, 3rem); font-weight: 700; line-height: 1.12; letter-spacing: -0.025em; }}
    .typo-h3 {{ font-family: 'Manrope', sans-serif; font-size: clamp(1.18rem, 1.7vw, 1.48rem); font-weight: 600; line-height: 1.25; }}
    .typo-eyebrow {{ font-size: 0.72rem; font-weight: 600; letter-spacing: 0.22em; text-transform: uppercase; }}

    .glass-nav {{ background: rgba(14, 36, 33, 0.52); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.12); transition: all 0.4s var(--ease); }}
    .glass-nav.scrolled {{ background: rgba(250, 248, 245, 0.96); border-bottom-color: rgba(14, 36, 33, 0.08); box-shadow: 0 10px 30px -12px rgba(14, 36, 33, 0.12); }}
    .glass-nav.scrolled .nav-link, .glass-nav.scrolled .brand-title {{ color: #0E2421 !important; }}
    .glass-nav.scrolled .brand-sub {{ color: #F1631C !important; }}

    .praan-btn {{ display: inline-flex; align-items: center; gap: 0.85rem; padding: 0.62rem 0.62rem 0.62rem 1.45rem; border-radius: 9999px; font-family: 'Manrope', sans-serif; font-size: 0.9rem; font-weight: 600; transition: transform 0.35s var(--ease); cursor: pointer; }}
    .praan-btn:hover {{ transform: translateY(-2px); }}
    .btn-circle {{ width: 2.3rem; height: 2.3rem; border-radius: 9999px; display: inline-flex; align-items: center; justify-content: center; transition: transform 0.4s var(--ease); }}
    .praan-btn:hover .btn-circle {{ transform: rotate(45deg); }}

    .hero-section {{ position: relative; min-height: 92vh; width: 100%; overflow: hidden; background: #0E2421; }}
    .hero-slide {{ position: absolute; inset: 0; opacity: 0; visibility: hidden; transition: opacity 1.1s var(--ease), visibility 1.1s; z-index: 1; }}
    .hero-slide.active {{ opacity: 1; visibility: visible; z-index: 2; }}
    .hero-slide-bg {{ position: absolute; inset: 0; background-size: cover; background-position: center; transform: scale(1.02); transition: transform 8s ease-out; }}
    .hero-slide.active .hero-slide-bg {{ transform: scale(1.08); }}
    .hero-scrim {{ position: absolute; inset: 0; background: linear-gradient(110deg, rgba(10, 26, 24, 0.86) 0%, rgba(10, 26, 24, 0.58) 55%, rgba(10, 26, 24, 0.35) 100%); z-index: 3; }}

    .hero-stagger {{ opacity: 0; transform: translateY(22px); transition: opacity 0.8s var(--ease), transform 0.8s var(--ease); }}
    .hero-slide.active .hero-stagger-1 {{ opacity: 1; transform: translateY(0); transition-delay: 0.15s; }}
    .hero-slide.active .hero-stagger-2 {{ opacity: 1; transform: translateY(0); transition-delay: 0.28s; }}
    .hero-slide.active .hero-stagger-3 {{ opacity: 1; transform: translateY(0); transition-delay: 0.42s; }}
    .hero-slide.active .hero-stagger-4 {{ opacity: 1; transform: translateY(0); transition-delay: 0.55s; }}

    .marquee-wrap {{ overflow: hidden; white-space: nowrap; }}
    .marquee-track {{ display: inline-flex; gap: 2.5rem; animation: marqueeScroll 32s linear infinite; }}
    @keyframes marqueeScroll {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}

    .reveal {{ opacity: 0; transform: translateY(28px); transition: opacity 0.8s var(--ease), transform 0.8s var(--ease); }}
    .reveal.is-visible {{ opacity: 1; transform: translateY(0); }}
    .hover-lift {{ transition: transform 0.4s var(--ease), box-shadow 0.4s var(--ease); }}
    .hover-lift:hover {{ transform: translateY(-5px); box-shadow: 0 22px 44px -18px rgba(14, 36, 33, 0.15); }}

    .sticky-tab {{ position: fixed; right: 0; top: 50%; transform: translateY(-50%); writing-mode: vertical-rl; z-index: 40; background: #F1631C; color: #fff; padding: 1rem 0.55rem; border-radius: 0.75rem 0 0 0.75rem; font-family: 'Manrope', sans-serif; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.2em; cursor: pointer; box-shadow: -4px 8px 20px rgba(241, 99, 28, 0.3); }}
  </style>
</head>
<body class="bg-ivory text-deepTeal antialiased">

  <!-- Sticky Glass Header -->
  <header id="mainNav" class="glass-nav fixed top-0 left-0 right-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
      <a href="#top" class="flex items-center gap-3 min-w-0">
        <span class="bg-white/95 px-3 py-1.5 rounded-xl shadow-md shrink-0 flex items-center gap-2.5">
          {svg_logo}
        </span>
        <div class="leading-tight min-w-0 hidden sm:block">
          <span class="brand-sub block text-[10px] tracking-[0.16em] text-praanOrange uppercase font-semibold whitespace-nowrap">{doctor_name} &bull; {city}</span>
        </div>
      </a>

      <nav class="hidden lg:flex items-center gap-8 text-sm font-medium">
        <a href="#care" class="nav-link text-white/90 hover:text-praanOrange transition">Specialties</a>
        <a href="#booking" class="nav-link text-white/90 hover:text-praanOrange transition">Book Appointment</a>
        <a href="#approach" class="nav-link text-white/90 hover:text-praanOrange transition">How It Works</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="tel:+{phone}" class="hidden sm:inline-flex text-xs font-semibold text-white/90 nav-link hover:text-praanOrange transition">{phone_display}</a>
        <button onclick="openModal()" class="praan-btn bg-praanOrange text-white hover:bg-white hover:text-deepTeal shadow-lg">
          <span class="hidden sm:inline">Book Consultation</span>
          <span class="sm:hidden">Book</span>
          <span class="btn-circle bg-deepTeal text-white">&#8599;</span>
        </button>
      </div>
    </div>
  </header>

  <button onclick="openModal()" class="sticky-tab hidden sm:block">BOOK VISIT</button>

  <!-- 3-SLIDE HERO -->
  <section id="top" class="hero-section flex items-end pb-14 sm:pb-24 pt-32 sm:pt-36">
    {slides_html}

    <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full flex items-center justify-between pt-8 pointer-events-none">
      <div class="flex items-center gap-2.5 pointer-events-auto">
        <button onclick="goToSlide(0)" class="hero-dot h-1.5 w-10 rounded-full bg-praanOrange transition-all" aria-label="Slide 1"></button>
        <button onclick="goToSlide(1)" class="hero-dot h-1.5 w-4 rounded-full bg-white/35 transition-all" aria-label="Slide 2"></button>
        <button onclick="goToSlide(2)" class="hero-dot h-1.5 w-4 rounded-full bg-white/35 transition-all" aria-label="Slide 3"></button>
      </div>
      <div class="hidden sm:flex items-center gap-3 pointer-events-auto">
        <button onclick="prevSlide()" class="w-10 h-10 rounded-full border border-white/25 bg-black/30 text-white hover:border-praanOrange flex items-center justify-center transition">&larr;</button>
        <button onclick="nextSlide()" class="w-10 h-10 rounded-full border border-white/25 bg-black/30 text-white hover:border-praanOrange flex items-center justify-center transition">&rarr;</button>
      </div>
    </div>
  </section>

  <!-- MARQUEE -->
  <div class="bg-deepTeal text-white border-y border-white/10 py-4">
    <div class="marquee-wrap">
      <div class="marquee-track typo-eyebrow text-xs">
        {marquee_html}
      </div>
    </div>
  </div>

  <!-- CARE PROGRAMS -->
  <section id="care" class="py-20 sm:py-28 bg-ivory">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-14 reveal">
        <div>
          <p class="typo-eyebrow text-praanOrange mb-3">Clinical Excellence &bull; {city}</p>
          <h2 class="typo-h2 text-deepTeal">Specialized Clinical Treatments</h2>
        </div>
        <div class="flex items-center gap-3 bg-white px-4 py-2.5 rounded-2xl border border-deepTeal/10 shadow-sm">
          {svg_logo}
          <div class="text-xs border-l border-deepTeal/10 pl-3">
            <strong class="block text-deepTeal">{doctor_name}</strong>
            <span class="text-slateInk">{rating} &bull; {reviews}</span>
          </div>
        </div>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {programs_html}
      </div>
    </div>
  </section>

  <!-- INTERACTIVE ONLINE APPOINTMENT BOOKING SYSTEM -->
  <section id="booking" class="py-20 sm:py-28 bg-deepTeal text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-5 reveal">
        <p class="typo-eyebrow text-praanOrange mb-3">Instant Online Booking</p>
        <h2 class="typo-h2 text-white mb-5">Schedule Your Consultation With {doctor_name}</h2>
        <p class="text-white/80 text-base leading-relaxed mb-8">
          Select your preferred treatment focus, visit mode, and time window below — your appointment request goes straight to our {city} clinic desk on WhatsApp.
        </p>
        <div class="grid grid-cols-3 gap-4 py-6 border-t border-white/15">
          <div>
            <div class="font-display font-bold text-2xl sm:text-3xl text-praanOrange">{rating}</div>
            <p class="text-xs text-white/70 mt-1">{reviews}</p>
          </div>
          <div>
            <div class="font-display font-bold text-2xl sm:text-3xl text-white">Zero</div>
            <p class="text-xs text-white/70 mt-1">Waiting Queue</p>
          </div>
          <div>
            <div class="font-display font-bold text-2xl sm:text-3xl text-praanOrange">100%</div>
            <p class="text-xs text-white/70 mt-1">Doctor-Led Care</p>
          </div>
        </div>
      </div>

      <div class="lg:col-span-7 reveal">
        <div class="bg-ivory text-deepTeal rounded-3xl p-6 sm:p-10 shadow-2xl">
          <div class="mb-5">
            <label class="block text-xs font-bold uppercase tracking-widest text-praanOrange mb-2.5">1. Select Treatment Focus</label>
            <div class="grid grid-cols-2 gap-2.5">
              {focus_buttons_html}
            </div>
          </div>

          <div class="mb-5">
            <label class="block text-xs font-bold uppercase tracking-widest text-praanOrange mb-2.5">2. Visit Mode</label>
            <div class="grid grid-cols-3 gap-2.5">
              {mode_buttons_html}
            </div>
          </div>

          <div class="grid sm:grid-cols-2 gap-3 mb-4">
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-praanOrange mb-1.5">3. Select Date</label>
              <input type="date" id="bookDate" class="w-full px-3.5 py-2.5 rounded-xl bg-white border border-deepTeal/15 text-sm font-medium" />
            </div>
            <div>
              <label class="block text-xs font-bold uppercase tracking-widest text-praanOrange mb-1.5">4. Patient Name</label>
              <input type="text" id="bookPatient" placeholder="e.g. Rajesh Sharma" class="w-full px-3.5 py-2.5 rounded-xl bg-white border border-deepTeal/15 text-sm" />
            </div>
          </div>

          <div class="mb-5">
            <label class="block text-xs font-bold uppercase tracking-widest text-praanOrange mb-2">5. Choose Exact Time Slot</label>
            <div class="space-y-2.5">
              <div>
                <span class="text-[11px] font-semibold text-slateInk uppercase tracking-wider block mb-1.5">Morning</span>
                <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5">
                  <button type="button" onclick="setSlot('09:30 AM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">09:30 AM</button>
                  <button type="button" onclick="setSlot('10:00 AM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-praanOrange text-xs font-semibold bg-praanOrange text-white transition">10:00 AM</button>
                  <button type="button" onclick="setSlot('10:30 AM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">10:30 AM</button>
                  <button type="button" onclick="setSlot('11:00 AM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">11:00 AM</button>
                  <button type="button" onclick="setSlot('11:30 AM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">11:30 AM</button>
                  <button type="button" onclick="setSlot('12:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">12:30 PM</button>
                </div>
              </div>
              <div>
                <span class="text-[11px] font-semibold text-slateInk uppercase tracking-wider block mb-1.5">Evening</span>
                <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5">
                  <button type="button" onclick="setSlot('04:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">04:30 PM</button>
                  <button type="button" onclick="setSlot('05:00 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">05:00 PM</button>
                  <button type="button" onclick="setSlot('05:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">05:30 PM</button>
                  <button type="button" onclick="setSlot('06:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">06:30 PM</button>
                  <button type="button" onclick="setSlot('07:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">07:30 PM</button>
                  <button type="button" onclick="setSlot('08:30 PM', this)" class="slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition">08:30 PM</button>
                </div>
              </div>
            </div>
          </div>

          <div id="slotSummary" class="mb-5 px-4 py-3 rounded-xl bg-praanSoft border border-praanOrange/25 text-xs text-deepTeal font-medium">
            Selected: <strong>{first_focus}</strong> &bull; <strong>{first_mode}</strong> &bull; <strong>10:00 AM</strong>
          </div>

          <button onclick="sendBooking()" class="w-full praan-btn bg-praanOrange text-white hover:bg-deepTeal justify-between shadow-lg">
            <span>Confirm Appointment Slot on WhatsApp</span>
            <span class="btn-circle bg-white text-deepTeal">&#8599;</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section id="approach" class="py-20 sm:py-28 bg-mist">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl mb-14 reveal">
        <p class="typo-eyebrow text-praanOrange mb-3">Patient-First Experience</p>
        <h2 class="typo-h2 text-deepTeal">Simple 3-Step Clinical Journey</h2>
      </div>
      <div class="grid md:grid-cols-3 gap-6">
        {steps_html}
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-deepTeal text-white pt-14 pb-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3.5">
        <span class="bg-white px-3 py-1.5 rounded-xl flex items-center gap-2">
          {svg_logo}
        </span>
        <div>
          <span class="text-xs tracking-[0.16em] text-praanOrange uppercase block">{doctor_name} &bull; {city}</span>
        </div>
      </div>
      <div class="text-center sm:text-right">
        <a href="tel:+{phone}" class="text-lg font-display font-semibold text-praanOrange hover:text-white transition block">{phone_display}</a>
        <p class="text-xs text-white/50 mt-1">&copy; 2026 {clinic_name}. All Rights Reserved.</p>
      </div>
    </div>
  </footer>

  <!-- MODAL -->
  <div id="consultModal" class="fixed inset-0 z-50 hidden items-center justify-center bg-black/70 backdrop-blur-sm p-4">
    <div class="bg-ivory text-deepTeal rounded-3xl max-w-md w-full p-6 sm:p-8 shadow-2xl relative">
      <button onclick="closeModal()" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-mist flex items-center justify-center">&times;</button>
      <div class="flex items-center gap-3.5 mb-5">
        <span class="bg-white px-2.5 py-1.5 rounded-xl border border-deepTeal/10">
          {svg_logo}
        </span>
        <div>
          <p class="typo-eyebrow text-praanOrange text-[10px]">{doctor_name}</p>
          <h3 class="font-display font-bold text-xl">Book Direct Consultation</h3>
        </div>
      </div>
      <form onsubmit="submitModal(event)" class="space-y-3.5">
        <input type="text" id="mName" required placeholder="Patient Full Name" class="w-full px-4 py-3 rounded-xl bg-white border border-deepTeal/15 text-sm" />
        <input type="text" id="mConcern" required placeholder="Concern / Treatment Needed" class="w-full px-4 py-3 rounded-xl bg-white border border-deepTeal/15 text-sm" />
        <button type="submit" class="w-full praan-btn bg-praanOrange text-white hover:bg-deepTeal justify-between">
          <span>Book via WhatsApp</span>
          <span class="btn-circle bg-white text-deepTeal">&#8599;</span>
        </button>
      </form>
    </div>
  </div>

  <script>
    const nav = document.getElementById('mainNav');
    window.addEventListener('scroll', () => nav.classList.toggle('scrolled', window.scrollY > 40), {{ passive: true }});

    let curSlide = 0;
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');
    function goToSlide(idx) {{
      slides[curSlide].classList.remove('active');
      dots[curSlide].classList.replace('w-10', 'w-4');
      dots[curSlide].classList.replace('bg-praanOrange', 'bg-white/35');
      curSlide = (idx + slides.length) % slides.length;
      slides[curSlide].classList.add('active');
      dots[curSlide].classList.replace('w-4', 'w-10');
      dots[curSlide].classList.replace('bg-white/35', 'bg-praanOrange');
    }}
    function nextSlide() {{ goToSlide(curSlide + 1); }}
    function prevSlide() {{ goToSlide(curSlide - 1); }}
    setInterval(nextSlide, 6000);

    const obs = new IntersectionObserver(es => es.forEach(e => {{ if (e.isIntersecting) e.target.classList.add('is-visible'); }}), {{ threshold: 0.12 }});
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

    let curFocus = '{first_focus}', curMode = '{first_mode}', curSlot = '10:00 AM';
    const dateInput = document.getElementById('bookDate');
    if (dateInput) {{
      const tomorrow = new Date(Date.now() + 86400000).toISOString().split('T')[0];
      dateInput.value = tomorrow;
      dateInput.min = new Date().toISOString().split('T')[0];
      dateInput.addEventListener('change', updateSummary);
    }}
    function updateSummary() {{
      const d = dateInput && dateInput.value ? dateInput.value : 'Upcoming';
      const el = document.getElementById('slotSummary');
      if (el) el.innerHTML = `Selected: <strong>${{curFocus}}</strong> &bull; <strong>${{curMode}}</strong> &bull; <strong>${{d}} at ${{curSlot}}</strong>`;
    }}
    function setFocus(val, btn) {{
      curFocus = val;
      document.querySelectorAll('.focus-btn').forEach(b => b.className = 'focus-btn py-2.5 px-3 rounded-xl border border-deepTeal/15 text-xs sm:text-sm font-semibold bg-white');
      btn.className = 'focus-btn py-2.5 px-3 rounded-xl border border-deepTeal text-xs sm:text-sm font-semibold bg-deepTeal text-white';
      updateSummary();
    }}
    function setMode(val, btn) {{
      curMode = val;
      document.querySelectorAll('.mode-btn').forEach(b => b.className = 'mode-btn py-2.5 px-3 rounded-xl border border-deepTeal/15 text-xs font-semibold bg-white');
      btn.className = 'mode-btn py-2.5 px-3 rounded-xl border border-deepTeal text-xs font-semibold bg-deepTeal text-white';
      updateSummary();
    }}
    function setSlot(val, btn) {{
      curSlot = val;
      document.querySelectorAll('.slot-btn').forEach(b => b.className = 'slot-btn py-2 px-1.5 rounded-lg border border-deepTeal/15 text-xs font-semibold bg-white hover:border-praanOrange transition');
      btn.className = 'slot-btn py-2 px-1.5 rounded-lg border border-praanOrange text-xs font-semibold bg-praanOrange text-white transition';
      updateSummary();
    }}
    updateSummary();
    function sendBooking() {{
      const d = dateInput && dateInput.value ? dateInput.value : 'Next Available';
      const patient = document.getElementById('bookPatient').value.trim() || 'Patient';
      const msg = `Hi {clinic_name}, I want to book an appointment for ${{patient}}. Treatment: ${{curFocus}} | Mode: ${{curMode}} | Date: ${{d}} | Time Slot: ${{curSlot}}.`;
      window.open(`https://wa.me/{phone}?text=${{encodeURIComponent(msg)}}`, '_blank');
    }}

    const modal = document.getElementById('consultModal');
    function openModal() {{ modal.classList.replace('hidden', 'flex'); }}
    function closeModal() {{ modal.classList.replace('flex', 'hidden'); }}
    function submitModal(e) {{
      e.preventDefault();
      const msg = `Hi {clinic_name}, I am ${{document.getElementById('mName').value}}. Looking for: ${{document.getElementById('mConcern').value}}.`;
      window.open(`https://wa.me/{phone}?text=${{encodeURIComponent(msg)}}`, '_blank');
      closeModal();
    }}
  </script>
</body>
</html>
"""

def build_svg_logo(title, sub, category):
    icon_path = (
        '<path d="M14 5c-2.8 0-4.8 1.9-4.8 4.8 0 2.6 1.1 5.4 1.8 8.3.3 1.2 1.2 1.8 1.9 1.2.7-.6 1-2.7 1.1-4.1.1-1 .8-1.4 1-1.4s.9.4 1 1.4c.1 1.4.4 3.5 1.1 4.1.7.6 1.6 0 1.9-1.2.7-2.9 1.8-5.7 1.8-8.3C18.8 6.9 16.8 5 14 5z" fill="#F1631C"/>'
        if category == "dental"
        else '<path d="M14 4.5c2.2 3.2 5 6.4 5 10.2a5 5 0 1 1-10 0c0-3.8 2.8-7 5-10.2z" fill="#F1631C"/>'
    )
    return f'''<span class="inline-flex items-center gap-2">
      <svg width="26" height="26" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="28" height="28" rx="8" fill="#FFF3EC"/>
        {icon_path}
      </svg>
      <span class="leading-none text-left">
        <span class="block font-display font-bold text-xs sm:text-sm text-[#0E2421] tracking-tight">{title}</span>
        <span class="block text-[9px] font-semibold tracking-widest text-[#F1631C] uppercase mt-0.5">{sub}</span>
      </span>
    </span>'''

def generate():
    for d in DOCTORS:
        slides_html = []
        for idx, (eyebrow, title, desc) in enumerate(d["hero"]):
            active = " active" if idx == 0 else ""
            bg = d["slides"][idx]
            cta = (
                '<a href="#booking" class="praan-btn bg-praanOrange text-white hover:bg-white hover:text-deepTeal shadow-xl"><span>Book Consultation</span><span class="btn-circle bg-deepTeal text-white">&#8599;</span></a><a href="#care" class="px-6 py-3.5 rounded-full border border-white/30 text-white text-sm font-medium hover:bg-white/10 transition">Explore Treatments</a>'
                if idx == 0 else
                '<a href="#booking" class="praan-btn bg-praanOrange text-white hover:bg-white hover:text-deepTeal"><span>Schedule Clinic Visit</span><span class="btn-circle bg-deepTeal text-white">&#8599;</span></a>'
            )
            tag = "h1" if idx == 0 else "h2"
            slides_html.append(f"""    <div class="hero-slide{active}" data-slide="{idx}">
      <div class="hero-slide-bg" style="background-image: url('{bg}');"></div>
      <div class="hero-scrim"></div>
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full pt-8">
        <div class="max-w-3xl">
          <div class="hero-stagger hero-stagger-1 inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-praanOrange/50 mb-6">
            <span class="w-2 h-2 rounded-full bg-praanOrange animate-pulse"></span>
            <span class="typo-eyebrow text-white">{eyebrow}</span>
          </div>
          <{tag} class="hero-stagger hero-stagger-2 typo-hero text-white mb-6">{title}</{tag}>
          <p class="hero-stagger hero-stagger-3 text-base sm:text-lg text-white/85 max-w-2xl leading-relaxed mb-8">{desc}</p>
          <div class="hero-stagger hero-stagger-4 flex flex-wrap gap-4">{cta}</div>
        </div>
      </div>
    </div>""")

        marquee_items = d["marquee"] * 2
        marquee_html = "".join(
            f'<span class="{"text-praanOrange" if i % 5 == 0 else ""}">{m}</span><span>&bull;</span>'
            for i, m in enumerate(marquee_items)
        )

        programs_html = []
        for badge, p_title, p_desc in d["programs"]:
            programs_html.append(f"""        <div class="bg-white p-7 rounded-3xl border border-deepTeal/8 hover-lift reveal">
          <span class="inline-block px-3 py-1 rounded-full bg-praanSoft text-praanOrange text-xs font-semibold mb-4">{badge}</span>
          <h3 class="typo-h3 text-deepTeal mb-2">{p_title}</h3>
          <p class="text-sm text-slateInk leading-relaxed mb-4">{p_desc}</p>
          <a href="#booking" class="text-xs font-semibold uppercase tracking-wider text-praanOrange">Book Slot &rarr;</a>
        </div>""")

        focus_buttons_html = []
        for i, f_opt in enumerate(d["focus_options"]):
            cls = "border-deepTeal bg-deepTeal text-white" if i == 0 else "border-deepTeal/15 bg-white"
            focus_buttons_html.append(f'<button type="button" onclick="setFocus(\'{f_opt}\', this)" class="focus-btn py-2.5 px-3 rounded-xl border text-xs sm:text-sm font-semibold {cls}">{f_opt}</button>')

        mode_buttons_html = []
        for i, m_opt in enumerate(d["modes"]):
            cls = "border-deepTeal bg-deepTeal text-white" if i == 0 else "border-deepTeal/15 bg-white"
            label = m_opt.split(" (")[0]
            mode_buttons_html.append(f'<button type="button" onclick="setMode(\'{m_opt}\', this)" class="mode-btn py-2.5 px-3 rounded-xl border text-xs font-semibold {cls}">{label}</button>')

        steps_html = []
        for i, (s_title, s_desc) in enumerate(d["steps"]):
            steps_html.append(f"""        <div class="bg-white p-7 rounded-3xl border border-deepTeal/8 hover-lift reveal">
          <span class="font-display font-bold text-3xl text-praanOrange block mb-4">0{i+1}</span>
          <h3 class="typo-h3 text-deepTeal mb-2">{s_title}</h3>
          <p class="text-sm text-slateInk leading-relaxed">{s_desc}</p>
        </div>""")

        html = TEMPLATE.format(
            clinic_name=d["clinic_name"],
            doctor_name=d["doctor_name"],
            degrees=d["degrees"],
            city=d["city"],
            phone=d["phone"],
            phone_display=d["phone_display"],
            rating=d["rating"],
            reviews=d["reviews"],
            svg_logo=build_svg_logo(d["logo_title"], d["logo_sub"], d["category"]),
            slides_html="\n".join(slides_html),
            marquee_html=marquee_html,
            programs_html="\n".join(programs_html),
            focus_buttons_html="\n              ".join(focus_buttons_html),
            mode_buttons_html="\n              ".join(mode_buttons_html),
            steps_html="\n".join(steps_html),
            first_focus=d["focus_options"][0],
            first_mode=d["modes"][0]
        )

        out_path = os.path.join(OUTPUT_DIR, f"{d['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Generated Praan-style clinic page:", out_path)

if __name__ == "__main__":
    generate()
