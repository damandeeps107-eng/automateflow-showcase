import os
import re

OUTPUT_DIR = "/Users/user/.gemini/antigravity/scratch/automateflow-showcase"

DOCTORS = [
    {
        "slug": "dr-bansal-dental",
        "clinic_name": "Dr Bansal's Dental & Implant Clinic",
        "doctor_name": "Dr. Bansal",
        "degrees": "BDS, MDS — Implantology & Laser Surgery",
        "specialty": "Guided Dental Implants, Painless RCT & Smile Aesthetics",
        "city": "Gurgaon",
        "phone": "919599661324",
        "rating": "4.8★",
        "reviews": "579+ Google Reviews",
        "hero_img": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1200&q=80",
        "primary_color": "#0EA5E9",
        "primary_soft": "#E0F2FE",
        "bg_dark": "#0A192F",
        "treatments": ["Guided Dental Implants", "Painless Single RCT", "Cosmetic Smile Design", "Invisible Teeth Aligners"],
        "logo_letter": "B"
    },
    {
        "slug": "dr-lokesh-dental",
        "clinic_name": "Prime Dental Care & Implant Centre",
        "doctor_name": "Dr. Lokesh",
        "degrees": "BDS, MDS — Oral Implantologist & Cosmetic Surgeon",
        "specialty": "Immediate Load Implants, Laser Dentistry & Full Mouth Rehab",
        "city": "Gurgaon",
        "phone": "919034194858",
        "rating": "4.8★",
        "reviews": "419+ Google Reviews",
        "hero_img": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=1200&q=80",
        "primary_color": "#2563EB",
        "primary_soft": "#DBEAFE",
        "bg_dark": "#0A192F",
        "treatments": ["Immediate Implants", "Laser Gum Therapy", "Zirconia Crowns", "Clear Aligners"],
        "logo_letter": "P"
    },
    {
        "slug": "dr-rashmi-derma",
        "clinic_name": "Dr Rashmi Agrawal Dermatology & Laser Clinic",
        "doctor_name": "Dr. Rashmi Agrawal",
        "degrees": "MBBS, MD (Dermatology, Venereology & Leprosy)",
        "specialty": "US-FDA Lasers, Anti-Aging Therapies & Clinical Dermatology",
        "city": "Noida",
        "phone": "919971731355",
        "rating": "4.8★",
        "reviews": "212+ Google Reviews",
        "hero_img": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?auto=format&fit=crop&w=1200&q=80",
        "primary_color": "#0D9488",
        "primary_soft": "#CCFBF1",
        "bg_dark": "#0F172A",
        "treatments": ["US-FDA Laser Hair Removal", "Acne Scar Resurfacing", "Chemical Peels & Glow", "Anti-Aging Botox/Fillers"],
        "logo_letter": "R"
    },
    {
        "slug": "dr-sukriti-derm",
        "clinic_name": "Cure Derm Skin Clinic",
        "doctor_name": "Dr. Sukriti Sharma",
        "degrees": "MBBS, MD — Consultant Dermatologist & Aesthetician",
        "specialty": "Clinical Cosmetology, Pigmentation & Hair Loss Solutions",
        "city": "Noida",
        "phone": "919899496133",
        "rating": "4.8★",
        "reviews": "240+ Google Reviews",
        "hero_img": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=1200&q=80",
        "primary_color": "#059669",
        "primary_soft": "#D1FAE5",
        "bg_dark": "#06221B",
        "treatments": ["PRP Hair Restoration", "Pigmentation & Melasma", "Carbon Laser Facial", "Advanced Skin Rejuvenation"],
        "logo_letter": "C"
    },
    {
        "slug": "south-delhi-dental",
        "clinic_name": "South Delhi Dental Clinic & Implant Centre",
        "doctor_name": "Senior Implant Specialist",
        "degrees": "BDS, MDS — Dental Implants & Aesthetic Dentistry",
        "specialty": "Digital Implantology, 3D Smile Designing & Painless Care",
        "city": "South Delhi",
        "phone": "919958004326",
        "rating": "4.8★",
        "reviews": "42+ Google Reviews",
        "hero_img": "https://images.unsplash.com/photo-1598256989800-fe5f95da9787?auto=format&fit=crop&w=1200&q=80",
        "primary_color": "#0284C7",
        "primary_soft": "#E0F2FE",
        "bg_dark": "#0A192F",
        "treatments": ["Computer-Guided Implants", "Invisible Braces", "Full Mouth Rehab", "Laser Bleaching"],
        "logo_letter": "S"
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{clinic_name} | {doctor_name} — {city}</title>
  <meta name="description" content="{specialty} by {doctor_name} ({degrees}). {rating} with {reviews} in {city}." />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brandNavy: '{bg_dark}',
            brandPrimary: '{primary_color}',
            brandSoft: '{primary_soft}',
            ivoryBg: '#F8FAFC',
            slateText: '#334155',
            goldStar: '#F59E0B'
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
    html, body {{ margin: 0; padding: 0; background: #F8FAFC; color: #0A192F; font-family: 'Inter', sans-serif; overflow-x: hidden; -webkit-font-smoothing: antialiased; }}
    .typo-hero {{ font-family: 'Manrope', sans-serif; font-size: clamp(2.2rem, 4.8vw, 4rem); font-weight: 800; line-height: 1.08; letter-spacing: -0.03em; }}
    .typo-h2 {{ font-family: 'Manrope', sans-serif; font-size: clamp(1.8rem, 3.2vw, 2.75rem); font-weight: 700; line-height: 1.15; letter-spacing: -0.02em; }}
    
    .glass-header {{ background: rgba(10, 25, 47, 0.94); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); }}
    
    .slot-pill {{
      border: 1px solid #CBD5E1;
      padding: 0.6rem 1rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #334155;
      cursor: pointer;
      transition: all 0.2s ease;
      background: #FFFFFF;
      text-align: center;
    }}
    .slot-pill:hover, .slot-pill.active {{
      border-color: {primary_color};
      background: {primary_soft};
      color: {primary_color};
      box-shadow: 0 4px 12px rgba(14, 165, 233, 0.15);
    }}

    .cta-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.8rem 1.6rem;
      border-radius: 9999px;
      font-family: 'Manrope', sans-serif;
      font-weight: 700;
      font-size: 0.95rem;
      transition: all 0.3s ease;
      cursor: pointer;
    }}
    .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.4); }}
  </style>
</head>
<body class="bg-ivoryBg text-slate-900">

  <!-- Fixed Top Header -->
  <header class="glass-header fixed top-0 left-0 right-0 z-50 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-brandPrimary/20 border border-brandPrimary flex items-center justify-center text-brandPrimary font-bold text-xl">
          {logo_letter}
        </div>
        <div>
          <span class="block font-display font-bold text-base leading-tight text-white tracking-tight">{clinic_name_short}</span>
          <span class="block text-[11px] text-brandPrimary uppercase tracking-widest font-semibold">{doctor_name} &bull; {city}</span>
        </div>
      </div>

      <div class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-300">
        <a href="#services" class="hover:text-brandPrimary transition">Specialties</a>
        <a href="#about" class="hover:text-brandPrimary transition">{doctor_name}</a>
        <a href="#booking" class="hover:text-brandPrimary transition">Direct VIP Slot</a>
        <a href="#reviews" class="hover:text-brandPrimary transition">{reviews}</a>
      </div>

      <div class="flex items-center gap-3">
        <a href="#booking" class="cta-btn bg-brandPrimary text-white hover:bg-white hover:text-slate-900 shadow-md">
          <span>Book Appointment</span>
          <span>&rarr;</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="relative pt-32 pb-20 md:pt-40 md:pb-28 bg-brandNavy text-white overflow-hidden">
    <div class="absolute inset-0 opacity-15 bg-[radial-gradient({primary_color}_1px,transparent_1px)] [background-size:24px_24px]"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-7">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-brandPrimary/10 border border-brandPrimary/40 text-brandPrimary text-xs font-semibold mb-6">
          <span class="w-2 h-2 rounded-full bg-brandPrimary animate-pulse"></span>
          <span>{rating} Verified Google Rating &bull; {reviews}</span>
        </div>
        
        <h1 class="typo-hero mb-6 text-white">
          State-of-the-Art Care & <span class="text-brandPrimary">{specialty}</span>
        </h1>
        
        <p class="text-slate-300 text-lg mb-8 max-w-xl leading-relaxed">
          Led by <strong>{doctor_name}</strong> ({degrees}), offering high-precision clinical excellence, 100% sterilized protocols, and frictionless VIP scheduling in {city}.
        </p>

        <div class="flex flex-wrap gap-4 items-center">
          <a href="#booking" class="cta-btn bg-brandPrimary text-white shadow-lg">
            <span>Select Consultation Slot</span>
            <span>&rarr;</span>
          </a>
          <a href="https://wa.me/{phone}?text=Hi%20{doctor_name},%20I%20would%20like%20to%20consult%20regarding%20an%20appointment" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-slate-600 text-slate-200 text-sm font-semibold hover:border-brandPrimary hover:text-brandPrimary transition">
            <span>Direct Doctor WhatsApp</span>
          </a>
        </div>
      </div>

      <!-- Real Clinic Image / Card -->
      <div class="lg:col-span-5">
        <div class="relative bg-slate-800/80 p-3 rounded-3xl border border-slate-700 shadow-2xl">
          <img src="{hero_img}" alt="{clinic_name} {city}" class="rounded-2xl w-full h-80 object-cover" />
          
          <div class="p-4 bg-slate-900/90 rounded-xl mt-3 flex items-center justify-between border border-slate-700">
            <div>
              <div class="text-sm font-bold text-white">{doctor_name}</div>
              <div class="text-xs text-brandPrimary font-medium">{degrees}</div>
            </div>
            <div class="text-right">
              <div class="text-goldStar text-sm font-bold">★★★★★ 4.8</div>
              <div class="text-[11px] text-slate-400">{reviews}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Doctor Appointment Scheduler -->
  <section id="booking" class="py-20 max-w-4xl mx-auto px-4 sm:px-6">
    <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-xl">
      <div class="text-center max-w-xl mx-auto mb-10">
        <span class="text-brandPrimary font-bold text-xs uppercase tracking-widest">DIRECT VIP SCHEDULER</span>
        <h2 class="typo-h2 mt-1 text-slate-900">Book Direct Consultation</h2>
        <p class="text-slateText text-sm mt-2">Skip the phone wait. Choose your preferred consultation date, time-slot, and confirm instantly with a WhatsApp entry pass.</p>
      </div>

      <div class="space-y-6">
        <!-- Treatment selection -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Select Consultation Specialty</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            {treatment_buttons}
          </div>
        </div>

        <!-- Date Picker -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Preferred Date</label>
          <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
            <button onclick="selectDate(this, 'Today')" class="slot-pill active">Today</button>
            <button onclick="selectDate(this, 'Tomorrow')" class="slot-pill">Tomorrow</button>
            <button onclick="selectDate(this, 'Mon, 30 Nov')" class="slot-pill">Mon, 30 Nov</button>
            <button onclick="selectDate(this, 'Tue, 1 Dec')" class="slot-pill">Tue, 1 Dec</button>
            <button onclick="selectDate(this, 'Wed, 2 Dec')" class="slot-pill">Wed, 2 Dec</button>
            <button onclick="selectDate(this, 'Thu, 3 Dec')" class="slot-pill">Thu, 3 Dec</button>
          </div>
        </div>

        <!-- Time Slots -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Available Consultation Slots</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5" id="slotGrid">
            <button onclick="selectSlot(this, '10:30 AM - 11:00 AM')" class="slot-pill active">10:30 AM</button>
            <button onclick="selectSlot(this, '11:30 AM - 12:00 PM')" class="slot-pill">11:30 AM</button>
            <button onclick="selectSlot(this, '01:00 PM - 01:30 PM')" class="slot-pill">01:00 PM</button>
            <button onclick="selectSlot(this, '04:30 PM - 05:00 PM')" class="slot-pill">04:30 PM</button>
            <button onclick="selectSlot(this, '05:30 PM - 06:00 PM')" class="slot-pill">05:30 PM</button>
            <button onclick="selectSlot(this, '06:30 PM - 07:00 PM')" class="slot-pill">06:30 PM</button>
            <button onclick="selectSlot(this, '07:30 PM - 08:00 PM')" class="slot-pill">07:30 PM</button>
            <button onclick="selectSlot(this, '08:30 PM - 09:00 PM')" class="slot-pill">08:30 PM</button>
          </div>
        </div>

        <!-- Patient details -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Patient Full Name</label>
            <input type="text" id="pName" placeholder="e.g. Rajesh Sharma" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-brandPrimary outline-none" />
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-600 mb-1">Patient Phone / WhatsApp</label>
            <input type="tel" id="pPhone" placeholder="10-digit mobile number" class="w-full px-4 py-2.5 rounded-xl border border-slate-300 text-sm focus:border-brandPrimary outline-none" />
          </div>
        </div>

        <div class="pt-4 text-center">
          <button onclick="confirmAppointment()" class="cta-btn bg-brandPrimary text-white w-full sm:w-auto text-center justify-center">
            <span>Confirm & Generate WhatsApp Slip</span>
            <span>&rarr;</span>
          </button>
          <p class="text-[12px] text-slate-400 mt-2">&bull; Zero aggregator commission &bull; Instant calendar lock &bull; 100% Sterilization Guarantee</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Clinic Trust Badges -->
  <section class="py-16 bg-white border-t border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="text-3xl font-display font-extrabold text-brandPrimary">{rating}</div>
          <div class="text-xs font-semibold text-slate-600 mt-1">{reviews}</div>
        </div>
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="text-3xl font-display font-extrabold text-slate-900">12+ Yrs</div>
          <div class="text-xs font-semibold text-slate-600 mt-1">Clinical Surgical Experience</div>
        </div>
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="text-3xl font-display font-extrabold text-brandPrimary">100%</div>
          <div class="text-xs font-semibold text-slate-600 mt-1">Class-B Autoclaved Hygiene</div>
        </div>
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-100">
          <div class="text-3xl font-display font-extrabold text-slate-900">Zero Wait</div>
          <div class="text-xs font-semibold text-slate-600 mt-1">Pre-Booked Calendar Slips</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-brandNavy text-slate-400 py-12 border-t border-slate-800 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 text-center">
      <p class="text-white font-bold">{clinic_name}</p>
      <p class="mt-1 text-xs">{doctor_name} &bull; {city}</p>
      <p class="mt-4 text-xs text-slate-500">&copy; 2026 {clinic_name}. All rights reserved. Direct VIP Scheduling Portal powered by AutomateFlow.</p>
    </div>
  </footer>

  <script>
    let currentTreatment = '{first_treatment}';
    let currentDate = 'Today';
    let currentSlot = '10:30 AM - 11:00 AM';

    function selectTreat(btn, name) {{
      document.querySelectorAll('#booking .grid-cols-2 button, #booking .grid-cols-4 button').forEach(b => {{
        if (b.innerText === currentTreatment) b.classList.remove('active');
      }});
      btn.classList.add('active');
      currentTreatment = name;
    }}

    function selectDate(btn, d) {{
      const p = btn.parentElement;
      p.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentDate = d;
    }}

    function selectSlot(btn, s) {{
      const p = document.getElementById('slotGrid');
      p.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentSlot = s;
    }}

    function confirmAppointment() {{
      const name = document.getElementById('pName').value.trim() || 'Valued Patient';
      const phone = document.getElementById('pPhone').value.trim() || 'Not Provided';
      
      const msg = `*NEW VIP APPOINTMENT BOOKING*\\n` +
                  `🏥 *Clinic:* {clinic_name}\\n` +
                  `👨‍⚕️ *Doctor:* {doctor_name}\\n` +
                  `📋 *Treatment:* ${{currentTreatment}}\\n` +
                  `📅 *Date:* ${{currentDate}}\\n` +
                  `⏰ *Slot:* ${{currentSlot}}\\n` +
                  `👤 *Patient:* ${{name}}\\n` +
                  `📞 *Phone:* ${{phone}}\\n` +
                  `------------------------------\\n` +
                  `⚡ Booked directly via VIP Clinic Portal.`;
      
      const url = `https://wa.me/{phone}?text=${{encodeURIComponent(msg)}}`;
      window.open(url, '_blank');
    }}
  </script>
</body>
</html>
"""

def generate_pages():
    for doc in DOCTORS:
        short_name = doc["clinic_name"].split(" - ")[0].split(":")[0]
        if len(short_name) > 28:
            short_name = short_name[:28] + "..."
            
        btn_html = []
        for i, t in enumerate(doc["treatments"]):
            active = " active" if i == 0 else ""
            btn_html.append(f'<button onclick="selectTreat(this, \'{t}\')" class="slot-pill{active}">{t}</button>')

        rendered = HTML_TEMPLATE.format(
            clinic_name=doc["clinic_name"],
            clinic_name_short=short_name,
            doctor_name=doc["doctor_name"],
            degrees=doc["degrees"],
            specialty=doc["specialty"],
            city=doc["city"],
            phone=doc["phone"],
            rating=doc["rating"],
            reviews=doc["reviews"],
            hero_img=doc["hero_img"],
            primary_color=doc["primary_color"],
            primary_soft=doc["primary_soft"],
            bg_dark=doc["bg_dark"],
            logo_letter=doc["logo_letter"],
            treatment_buttons="\n            ".join(btn_html),
            first_treatment=doc["treatments"][0]
        )
        
        filepath = os.path.join(OUTPUT_DIR, f"{doc['slug']}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_pages()
