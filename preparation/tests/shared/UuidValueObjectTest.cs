/* 
 * 
 * Libraries
 *
*/

using NUnit.Framework;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.tests.shared {

    [TestFixture]
    public class UuidValueObjectTest {

        /* 
         * 
         * Methods
         *
        */

        [Test]
        public void testIsNotAnEqualObject() {
            // Variables
            UuidValueObject valueObject;
            bool            response;
            // Code
            valueObject = new UuidValueObject( "56de485d-304e-41a3-b822-d129e464a1ea" );
            response    = valueObject.equals( new UuidValueObject( "56de485d-304e-41a3-b822-d129e464a1ee" ) );
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAnEqualObject() {
            // Variables
            UuidValueObject valueObject;
            bool            response;
            // Code
            valueObject = new UuidValueObject( "56de485d-304e-41a3-b822-d129e464a1ea" );
            response    = valueObject.equals( new UuidValueObject( "56de485d-304e-41a3-b822-d129e464a1ea" ) );
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsAnEmptyObject() {
            // Variables
            UuidValueObject valueObject;
            bool            response;
            // Code
            valueObject = new UuidValueObject( "" );
            response    = valueObject.isEmpty();
            Assert.IsTrue( response );
        }

        [Test]
        public void testIsNotAnEmptyObject() {
            // Variables
            UuidValueObject valueObject;
            bool            response;
            // Code
            valueObject = new UuidValueObject( "56de485d-304e-41a3-b822-d129e464a1ea" );
            response    = valueObject.isEmpty();
            Assert.IsFalse( response );
        }

        [Test]
        public void testIsAGeneratedValue() {
            // Variables
            UuidValueObject valueObject;
            string          value;
            // Code
            valueObject = new UuidValueObject( "hello world!" );
            value       = valueObject.getValue();
            Assert.AreNotEqual( value, "" );
        }

    }

}