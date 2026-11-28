import json
import os
import re

OUTPUT_DIR = "/Users/user/.gemini/antigravity/scratch/automateflow-showcase"
BATCH3_FILE = "/Users/user/.gemini/antigravity/scratch/batch3_doctors.json"

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

from generate_doctor_portal_pages import TEMPLATE, build_svg_logo

BATCH3_CLINICS = [
    {
        "clinic_name": "Dr. Jain's Dental and Implant Clinic",
        "doctor_name": "Dr. Jain",
        "city": "Janakpuri, Delhi",
        "phone": "918527105550",
        "rating": "4.9★",
        "reviews": "Active Clinic",
        "category": "dental"
    },
    {
        "clinic_name": "Dr. Megha Sharma MD Dermatology Clinic",
        "doctor_name": "Dr. Megha Sharma",
        "city": "Delhi",
        "phone": "919910662245",
        "rating": "4.9★",
        "reviews": "MD Dermatology",
        "category": "derma"
    },
    {
        "clinic_name": "Delhi Laser Clinic",
        "doctor_name": "Delhi Laser Clinic Team",
        "city": "Delhi",
        "phone": "919711833331",
        "rating": "4.8★",
        "reviews": "Laser & Skin Care",
        "category": "derma"
    },
    {
        "clinic_name": "SARA Skin & Laser Clinic",
        "doctor_name": "SARA Skin Team",
        "city": "Jalandhar",
        "phone": "919501103882",
        "rating": "4.8★",
        "reviews": "597+ Reviews",
        "category": "derma"
    },
    {
        "clinic_name": "Dentocare",
        "doctor_name": "Dentocare Team",
        "city": "Chandigarh",
        "phone": "918700746141",
        "rating": "4.8★",
        "reviews": "566+ Reviews",
        "category": "dental"
    },
    {
        "clinic_name": "Blue Shine Dental Clinic",
        "doctor_name": "Blue Shine Dental Team",
        "city": "Delhi",
        "phone": "919599582158",
        "rating": "4.8★",
        "reviews": "393+ Reviews",
        "category": "dental"
    },
    {
        "clinic_name": "Bansal Dental Clinic",
        "doctor_name": "Dr. Bansal",
        "city": "Rohini, Delhi",
        "phone": "919811254065",
        "rating": "4.8★",
        "reviews": "327+ Reviews",
        "category": "dental"
    },
    {
        "clinic_name": "Divine Dental Art",
        "doctor_name": "Divine Dental Team",
        "city": "Delhi",
        "phone": "917428221570",
        "rating": "4.8★",
        "reviews": "258+ Reviews",
        "category": "dental"
    },
    {
        "clinic_name": "Dr Supriya Chopra Skin Clinic",
        "doctor_name": "Dr. Supriya Chopra",
        "city": "Jalandhar",
        "phone": "918968920099",
        "rating": "4.8★",
        "reviews": "196+ Reviews",
        "category": "derma"
    },
    {
        "clinic_name": "Sanjeevani Dental & Implant Clinic",
        "doctor_name": "Sanjeevani Dental Team",
        "city": "Chandigarh",
        "phone": "918091222277",
        "rating": "4.8★",
        "reviews": "185+ Reviews",
        "category": "dental"
    }
]

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')[:40].strip('-')

def main():
    manifest = []
    for item in BATCH3_CLINICS:
        name = item["clinic_name"]
        doc_name = item["doctor_name"]
        city = item["city"]
        phone = item["phone"]
        phone_display = f"+91 {phone[2:7]} {phone[7:]}"
        rating = item["rating"]
        reviews = item["reviews"]
        category = item["category"]
        slides = DENTAL_SLIDES if category == "dental" else DERMA_SLIDES
        slug = slugify(name)
        short_logo = name if len(name) <= 22 else " ".join(name.split()[:3])

        if category == "dental":
            sub = f"IMPLANT & DENTAL • {city.upper()}"
            hero = [
                (f"{rating} Verified • {reviews} • {city}", f"Precision Dental <span class='text-praanOrange'>Implants</span> & Painless Care.", f"{name} in {city} — trusted for computer-guided dental implants, single-sitting root canals, and invisible aligners."),
                ("Digital 3D Smile Design", "Restore Your <span class='text-praanOrange'>Natural Smile</span> Comfortably.", "100% Class-B autoclaved sterilization, gentle anesthesia, and natural zirconia crowns crafted to last."),
                ("Direct VIP Appointment Portal", "Skip The <span class='text-praanOrange'>Waiting Room</span> Queue.", f"Book your preferred consultation slot directly with {name} and get an instant WhatsApp pass.")
            ]
            marquee = [name.upper(), f"{rating} ({reviews.upper()})", "GUIDED DENTAL IMPLANTS", "PAINLESS SINGLE-SITTING RCT", f"{city.upper()} CLINIC"]
            programs = [
                ("Implants", "Guided Dental Implants", "Computer-assisted titanium & Swiss implants with lifelong structural stability."),
                ("Endodontics", "Painless Single-Sitting RCT", "Microscopic, painless root canal treatment completed comfortably in one sitting."),
                ("Aesthetics", "Invisible Aligners & Veneers", "3D digital smile designing with clear aligners and ultra-thin porcelain veneers."),
                ("Oral Surgery", "Full Mouth Rehabilitation", "Minimally invasive surgical extractions and fixed teeth implant solutions.")
            ]
            focus_options = ["Dental Implants", "Painless RCT", "Clear Aligners", "Smile Design"]
            modes = [f"Clinic Visit ({city})", "Video Consult", "Priority Implant Slot"]
            steps = [
                ("3D Digital Scan & Checkup", f"Detailed intraoral evaluation & digital X-ray review at {name}."),
                ("Transparent Treatment Plan", "Clear timeline, painless protocol, and zero hidden charges before starting."),
                ("Sterilized Precision Care", "World-class implant & restorative execution with automated WhatsApp follow-up.")
            ]
        else:
            sub = f"SKIN & LASER • {city.upper()}"
            hero = [
                (f"{rating} Verified • {reviews} • {city}", f"Clinical <span class='text-praanOrange'>Dermatology</span> & US-FDA Lasers.", f"{name} in {city} — trusted for evidence-based skin rejuvenation, laser hair removal, and anti-aging care."),
                ("Skin & Laser Mastery", "Restore Natural <span class='text-praanOrange'>Radiance</span> Safely.", "Doctor-guided chemical peels, acne scar resurfacing, pigmentation care, and medical facials."),
                ("Direct VIP Appointment Portal", f"Book Direct With <span class='text-praanOrange'>{short_logo}</span>.", "Select your preferred consultation slot below and get an instant WhatsApp booking pass.")
            ]
            marquee = [name.upper(), f"{rating} ({reviews.upper()})", "US-FDA LASER CARE", "ACNE & PIGMENTATION", f"{city.upper()} CLINIC"]
            programs = [
                ("Laser Care", "US-FDA Laser Hair Removal", "Comfortable, safe triple-wavelength laser sessions for Indian skin tones."),
                ("Skin Clarity", "Acne, Scars & Melasma", "Medical-grade peels, MNRF, and targeted protocols for clear, even skin."),
                ("Anti-Aging", "Medi-Facials & Glow", "HydraFacial MD, carbon laser facials, and collagen-boosting therapies."),
                ("Hair Care", "PRP & GFC Hair Therapy", "Clinical scalp therapies to control hair fall and restore thickness.")
            ]
            focus_options = ["Acne & Pigmentation", "Laser Hair Removal", "Medi-Facial / Glow", "Hair Fall / PRP"]
            modes = [f"Clinic Visit ({city})", "Video Skin Consult", "Laser Session"]
            steps = [
                ("In-Depth Skin Analysis", f"Root-cause dermatological assessment at {name}."),
                ("Personalized Skin Roadmap", "Safe blend of clinical actives, US-FDA lasers, and daily home care."),
                ("Visible, Safe Results", "Tracked session-by-session improvements with WhatsApp care support.")
            ]

        slides_html = []
        for idx, (eyebrow, title, desc) in enumerate(hero):
            active = " active" if idx == 0 else ""
            bg = slides[idx]
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

        marquee_items = marquee * 2
        marquee_html = "".join(
            f'<span class="{"text-praanOrange" if i % 5 == 0 else ""}">{m}</span><span>&bull;</span>'
            for i, m in enumerate(marquee_items)
        )

        programs_html = [
            f"""        <div class="bg-white p-7 rounded-3xl border border-deepTeal/8 hover-lift reveal">
          <span class="inline-block px-3 py-1 rounded-full bg-praanSoft text-praanOrange text-xs font-semibold mb-4">{badge}</span>
          <h3 class="typo-h3 text-deepTeal mb-2">{p_title}</h3>
          <p class="text-sm text-slateInk leading-relaxed mb-4">{p_desc}</p>
          <a href="#booking" class="text-xs font-semibold uppercase tracking-wider text-praanOrange">Book Slot &rarr;</a>
        </div>"""
            for badge, p_title, p_desc in programs
        ]

        focus_buttons_html = [
            f'<button type="button" onclick="setFocus(\'{f_opt}\', this)" class="focus-btn py-2.5 px-3 rounded-xl border text-xs sm:text-sm font-semibold {"border-deepTeal bg-deepTeal text-white" if i == 0 else "border-deepTeal/15 bg-white"}">{f_opt}</button>'
            for i, f_opt in enumerate(focus_options)
        ]

        mode_buttons_html = [
            f'<button type="button" onclick="setMode(\'{m_opt}\', this)" class="mode-btn py-2.5 px-3 rounded-xl border text-xs font-semibold {"border-deepTeal bg-deepTeal text-white" if i == 0 else "border-deepTeal/15 bg-white"}">{m_opt.split(" (")[0]}</button>'
            for i, m_opt in enumerate(modes)
        ]

        steps_html = [
            f"""        <div class="bg-white p-7 rounded-3xl border border-deepTeal/8 hover-lift reveal">
          <span class="font-display font-bold text-3xl text-praanOrange block mb-4">0{i+1}</span>
          <h3 class="typo-h3 text-deepTeal mb-2">{s_title}</h3>
          <p class="text-sm text-slateInk leading-relaxed">{s_desc}</p>
        </div>"""
            for i, (s_title, s_desc) in enumerate(steps)
        ]

        html = TEMPLATE.format(
            clinic_name=name,
            doctor_name=doc_name,
            degrees=f"{rating} Verified Clinic",
            city=city,
            phone=phone,
            phone_display=phone_display,
            rating=rating,
            reviews=reviews,
            svg_logo=build_svg_logo(short_logo, sub, category),
            slides_html="\n".join(slides_html),
            marquee_html=marquee_html,
            programs_html="\n".join(programs_html),
            focus_buttons_html="\n              ".join(focus_buttons_html),
            mode_buttons_html="\n              ".join(mode_buttons_html),
            steps_html="\n".join(steps_html),
            first_focus=focus_options[0],
            first_mode=modes[0]
        )

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        manifest.append({
            "slug": slug,
            "doctor_name": doc_name,
            "clinic_name": name,
            "reviews": f"{reviews}, {rating}",
            "phone": phone
        })
        print(f"Generated: {slug}.html -> {phone}")

    with open(BATCH3_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Saved Batch 3 manifest ({len(manifest)} clinics)")

if __name__ == "__main__":
    main()
