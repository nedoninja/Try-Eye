using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Try_Eye
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
            string txt = File.ReadAllText("services\\doctor.txt");
            string[] wd = txt.Split(new char[] { ' ' });
            textBox2.Text = wd[0];
            textBox1.Text = wd[1];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            File.WriteAllText("services\\doctor.txt", string.Empty);
            File.WriteAllText("services\\doctor.txt", textBox2.Text + " " + textBox1.Text);
            var fm = new Form2();
            fm.Show();
            Hide();
        }
    }
}
