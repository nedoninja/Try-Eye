using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Try_Eye
{
    public partial class Form2 : Form
    {
        public bool isCkc = false;
        public Form2()
        {
            InitializeComponent();
            label1.Visible = false;

            pictureBox1.Visible = true;
            pictureBox2.Visible = true;
            pictureBox3.Visible = true;

            button1.Visible = true;
            button2.Visible = true;

            label2.Visible = false;

            label3.Visible = false;
            label4.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String res = run_cmd("\"services\\venv\\Scripts\\python.exe\"", "\"services\\Doctor.py\"");
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var fm = new Form3();
            fm.Show();
            Hide();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            String res = run_cmd("\"services\\venv\\Scripts\\python.exe\"", "\"services\\Glass.py\"");
            label2.Visible = true;
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            String res = run_cmd("\"services\\venv\\Scripts\\python.exe\"", "\"services\\Acuity.py\"");
            label3.Text = res;
            label3.Visible = true;
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            String res = run_cmd("\"services\\venv\\Scripts\\python.exe\"", "\"services\\IPD.py\"");
            label4.Text = res;
            label4.Visible = true;
        }

        private String run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.WindowStyle = ProcessWindowStyle.Hidden;
            start.FileName = cmd;
            start.Arguments = args;
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return result;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (!isCkc)
            {
                label1.Visible = true;
                pictureBox1.Visible = false;
                pictureBox2.Visible = false;
                pictureBox3.Visible = false;

                button1.Visible = false;
                button2.Visible = false;
                isCkc = true;
            }
            else if (isCkc)
            {
                label1.Visible = false;
                pictureBox1.Visible = true;
                pictureBox2.Visible = true;
                pictureBox3.Visible = true;

                button1.Visible = true;
                button2.Visible = true;
                isCkc = false;
            }
        }
    }
}
