# 🎨 MagangHub Analytics — Design Guide

## Quick Reference untuk Design System

### 🎯 Design Philosophy
**"From Opportunity to Competition"**

Dashboard ini dirancang sebagai **editorial data storytelling platform**, bukan admin dashboard biasa. Visual yang profesional, restrained, dan fokus pada data.

---

## 🎨 Design Tokens

### Colors
```css
/* Primary Palette */
--color-primary: #1E40AF      /* Deep Blue - Main actions, emphasis */
--color-secondary: #3B82F6    /* Sky Blue - Secondary elements */
--color-accent: #D97706        /* Amber - Highlights, CTAs */

/* Neutrals */
--color-background: #F8FAFC   /* Warm off-white */
--color-foreground: #1E3A8A   /* Navy - Main text */
--color-muted: #E9EEF6        /* Light blue-gray - Backgrounds */
--color-border: #DBEAFE       /* Light blue - Dividers */

/* Semantic */
--color-success: #059669      /* Green - Growth, opportunity */
--color-warning: #F59E0B      /* Bright amber */
--color-destructive: #DC2626  /* Red - Competition, danger */
```

### Typography
```css
/* Fonts */
Headings: 'Fira Code', monospace    /* Technical, editorial */
Body:     'Fira Sans', sans-serif   /* Clean, readable */

/* Scale */
h1: 1.875rem (30px)
h2: 1.5rem   (24px)
h3: 1.25rem  (20px)
Body: 1rem   (16px)
Small: 0.875rem (14px)
Tiny: 0.75rem (12px)
```

### Spacing Scale
```
--space-xs:  4px
--space-sm:  8px
--space-md:  16px
--space-lg:  24px
--space-xl:  32px
--space-2xl: 48px
--space-3xl: 64px
```

---

## 📊 Chart Color Guidelines

### When to Use Each Color:

**Blue Gradient** → Default, neutral data
```python
color_continuous_scale=[[0, '#DBEAFE'], [0.5, '#3B82F6'], [1, '#1E40AF']]
```

**Green Gradient** → Growth, opportunities, positives
```python
color_continuous_scale=[[0, '#D1FAE5'], [0.5, '#10B981'], [1, '#059669']]
```

**Amber Gradient** → Highlights, applicants, demand
```python
color_continuous_scale=[[0, '#FED7AA'], [0.5, '#F59E0B'], [1, '#D97706']]
```

**Red Gradient** → Competition, intensity, warnings
```python
color_continuous_scale=[[0, '#FEE2E2'], [0.5, '#EF4444'], [1, '#DC2626']]
```

**Categorical** → Multiple categories without semantic meaning
```python
color_discrete_sequence=CHART_COLORS['categorical']
# ['#1E40AF', '#3B82F6', '#8B5CF6', '#EC4899', '#F59E0B', '#10B981']
```

### Chart Template
```python
import plotly.express as px

fig = px.bar(
    data,
    x='category',
    y='value',
    color='value',
    color_continuous_scale=[[0, '#DBEAFE'], [0.5, '#3B82F6'], [1, '#1E40AF']]
)

fig.update_layout(
    font=dict(family="Fira Sans, sans-serif"),
    title_font=dict(size=16, family="Fira Code, monospace", color="#1E3A8A"),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
```

---

## 🚫 What NOT to Do

### ❌ Don't Add Icons or Emojis
```python
# ❌ BAD
st.header("📊 Analysis Dashboard")
tab1 = st.tab("🏢 Instansi")

# ✅ GOOD
st.markdown("## Analysis Dashboard")
tab1 = st.tab("Instansi")
```

### ❌ Don't Use Random Colors
```python
# ❌ BAD
marker_color='lightblue'
color_discrete_sequence=px.colors.qualitative.Set3

# ✅ GOOD
marker_color=CHART_COLORS['primary']
color_discrete_sequence=CHART_COLORS['categorical']
```

### ❌ Don't Break Typography Hierarchy
```python
# ❌ BAD - Skipping levels
st.markdown("# Title")
st.markdown("### Subtitle")  # Skipped h2

# ✅ GOOD
st.markdown("# Title")
st.markdown("## Subtitle")
st.markdown("### Section")
```

### ❌ Don't Use Arbitrary Spacing
```python
# ❌ BAD
st.markdown("<div style='margin-top: 13px'>")

# ✅ GOOD - Use design tokens
st.markdown("<div style='margin-top: var(--space-md)'>")
```

---

## ✅ Best Practices

### 1. Maintain Visual Hierarchy
```markdown
# Page Title (h1) - Once per page
## Section Title (h2) - Major sections
### Subsection (h3) - Within sections
**Bold** - Emphasis within body text
```

### 2. Use Consistent Spacing
```python
# After major sections
st.markdown("---")  # Adds proper divider

# Between related elements
st.markdown("")  # One line break

# For emphasis
st.markdown("<br>", unsafe_allow_html=True)  # Extra space
```

### 3. Chart Consistency
Every chart should have:
- Consistent font (Fira Sans/Fira Code)
- Transparent background
- Colors from design system
- Proper title sizing (16px Fira Code)

### 4. KPI Cards
```python
# ✅ Clean metric without delta
st.metric(
    label="Total Lowongan",
    value=f"{count:,}"
)

# ❌ Don't use misleading delta
st.metric(
    label="Total Lowongan",
    value=f"{filtered_count:,}",
    delta=f"{filtered_count - total_count}"  # Misleading!
)
```

### 5. Buttons and Actions
```python
# Primary action
st.button("Analyze Data")  # Uses primary blue

# Download action
st.download_button("Download CSV", data)  # Uses amber accent
```

---

## 🎯 Component Examples

### Section Header
```python
st.markdown("## Analisis Berdasarkan Instansi")
```

### Subsection with Context
```python
st.markdown("### Top 15 Provinsi — Jumlah Lowongan")
st.caption("Provinsi dengan konsentrasi lowongan tertinggi")
```

### Info Box
```python
st.info("💡 **Tips**: Gunakan filter untuk analisis lebih spesifik")
```

### Data Display
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rata-rata", f"{avg:.2f}")
with col2:
    st.metric("Median", f"{median:.0f}")
with col3:
    st.metric("Maksimum", f"{max:.0f}")
```

---

## 🔧 Making Changes

### Change Primary Color
Edit `:root` CSS variables:
```css
--color-primary: #YOUR_COLOR;
```

### Change Fonts
Update Google Fonts import and variables:
```css
@import url('https://fonts.googleapis.com/css2?family=Your+Font');
--font-heading: 'Your Font', sans-serif;
```

### Adjust Spacing
Modify spacing scale:
```css
--space-md: 20px;  /* Default is 16px */
```

### Add New Chart Color Scheme
Update `CHART_COLORS` dictionary:
```python
CHART_COLORS = {
    'primary': '#1E40AF',
    'your_new_scheme': '#YOUR_COLOR',
    # ...
}
```

---

## 📐 Layout Guidelines

### Max Content Width
```css
max-width: 1400px;  /* Defined in .block-container */
```

### Column Layouts
```python
# Equal columns
col1, col2 = st.columns(2)

# Weighted columns
col1, col2 = st.columns([2, 1])  # 2:1 ratio

# Three columns for metrics
col1, col2, col3 = st.columns(3)

# Five columns for KPIs
col1, col2, col3, col4, col5 = st.columns(5)
```

### Responsive Breakpoints
```css
@media (max-width: 768px) {
    /* Mobile adjustments */
}
```

---

## 🎨 Color Psychology

| Color | Use Case | Meaning |
|-------|----------|---------|
| **Blue** | Data, institutions, neutral facts | Trust, professionalism, stability |
| **Amber** | Highlights, applicants, CTAs | Energy, warmth, attention |
| **Red** | Competition, intensity, danger | Urgency, warning, high stakes |
| **Green** | Growth, opportunities, success | Positive, opportunity, go |
| **Purple** | Categories, variety | Creative, diverse, unique |

---

## 📱 Accessibility

### Text Contrast
- Body text: ≥4.5:1 contrast ratio
- Large text (≥18pt): ≥3:1 contrast ratio
- Current system: 4.5:1+ throughout ✅

### Focus States
All interactive elements have visible focus indicators for keyboard navigation.

### Reduced Motion
Animations respect `prefers-reduced-motion` media query.

---

## 🚀 Performance

### Chart Optimization
```python
# For large datasets, sample before plotting
df_sample = df.sample(n=min(1000, len(df)), random_state=42)
```

### Caching
```python
@st.cache_data
def load_data():
    # Expensive data loading
    return df
```

---

## 📚 Resources

- **UI/UX Pro Max**: Design system source
- **Google Fonts**: https://fonts.google.com/specimen/Fira+Sans
- **Plotly Colors**: Custom gradients defined in CHART_COLORS
- **Streamlit Docs**: https://docs.streamlit.io/

---

## ✨ Remember

1. **No icons/emojis** - Ever. Typography only.
2. **Use design system colors** - Don't invent new ones.
3. **Follow spacing scale** - Keep rhythm consistent.
4. **Typography hierarchy** - h1 → h2 → h3, don't skip.
5. **Chart consistency** - Same fonts and backgrounds.

---

**Last Updated:** October 10, 2026  
**Design System Version:** 1.0  
**Status:** Production Ready ✅
